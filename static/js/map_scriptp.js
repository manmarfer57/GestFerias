import { initMap } from "./map_utils.js";

document.addEventListener("DOMContentLoaded", function () {
    const mapData = document.getElementById("map-data");
    const latitud = parseFloat(mapData.dataset.latitud) || 37.388630;
    const longitud = parseFloat(mapData.dataset.longitud) || -5.995340;

    function redirigirAParcela(parcelaId) {
        window.location.href = `/parcela/${parcelaId}`;
    }

    const map = initMap("map", latitud, longitud);
    if (map) {
        const parcelas = JSON.parse(document.getElementById("parcelas-data")?.textContent || "[]");
        parcelas.forEach(parcela => {
            if (parcela.localizacion && Array.isArray(parcela.localizacion[0])) {
                L.geoJSON({
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": { "type": "Polygon", "coordinates": parcela.localizacion },
                        "properties": { "name": parcela.nombre }
                    }]
                }, {
                    style: { color: 'black', fillColor: 'black', fillOpacity: 0.5 },
                    onEachFeature: function (feature, layer) {
                        //Muestro un tooltip informativo con nombre y detalles de la parcela al pasar el ratón (no permanente)
                        layer.bindTooltip(parcela.nombre + ", " + parcela.detalles, { permanent: false, direction: 'top' });

                        //Ajusto la vista al polígono clicado y se dispara la redirección, combinando interacción visual y navegación
                        layer.on('click', function () {
                            map.fitBounds(layer.getBounds());
                            redirigirAParcela(parcela.id);
                        });
                    }
                }).addTo(map);
            }
        });
    }
});

