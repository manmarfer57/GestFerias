import { initMap, loadParcelas } from "./map_utils.js";

document.addEventListener("DOMContentLoaded", function () {
    const mapData = document.getElementById("map-data");
    const latitud = parseFloat(mapData.getAttribute("data-latitud"));
    const longitud = parseFloat(mapData.getAttribute("data-longitud"));

    const map = initMap("map", latitud, longitud);

    if (map) {
        const drawnItems = new L.FeatureGroup();
        map.addLayer(drawnItems);

        //Herramientas de dibujo
        map.addControl(new L.Control.Draw({
            edit: { featureGroup: drawnItems },
            draw: {
                polygon: { shapeOptions: { color: 'black', weight: 1, fillOpacity: 0.5 } },
                rectangle: { shapeOptions: { color: "black", weight: 1 } },
                polyline: false, circle: false, circlemarker: false, marker: false
            }
        }));

        map.on('draw:created', function (e) {
            //Solo una geometría activa a la vez; limpio antes de añadir la nueva
            drawnItems.clearLayers();
            drawnItems.addLayer(e.layer);
            //Convierto el objeto dibujado a formato GeoJSON y guardo solo las coordenadas en un input oculto para envío
            document.getElementById('coordenadas').value = JSON.stringify(e.layer.toGeoJSON().geometry.coordinates);
        });

        const parcelas = JSON.parse(document.getElementById("parcelas-data")?.textContent || "[]");
        loadParcelas(map, parcelas);
    }
});
