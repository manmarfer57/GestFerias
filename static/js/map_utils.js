export function initMap(containerId, lat, lng, zoom = 15) {
    if (!document.getElementById(containerId)) return null;

    //Carga mapas base de OpenStreetMap
    const map = L.map(containerId).setView([lat, lng], zoom);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    return map;
}

export function loadParcelas(map, parcelas) {
    parcelas.forEach(parcela => {
        if (parcela.localizacion && Array.isArray(parcela.localizacion[0])) { // Verifica si la localización es un array de arrays (coordenadas)
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
                    layer.bindTooltip(parcela.nombre, { permanent: false, direction: 'top' });
                }
            }).addTo(map);
        }
    });
}

export function loadGeoJSON(map, geoJsonData) {
    if (geoJsonData.length > 0) {
        const parcelLayer = L.geoJSON({
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": { "type": "Polygon", "coordinates": geoJsonData },
                    "properties": { "name": "Área Seleccionada" }
                }
            ]
        }, {
            style: { color: 'black', fillColor: 'black', fillOpacity: 0.5 }
        }).addTo(map);
        map.fitBounds(parcelLayer.getBounds());
    } else {
        console.error('No hay coordenadas GeoJSON válidas');
    }
}
