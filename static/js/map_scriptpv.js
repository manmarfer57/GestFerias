import { initMap, loadGeoJSON } from "./map_utils.js";

document.addEventListener("DOMContentLoaded", function () {
    const containerId = 'map';
    const defaultLat = 38.059819;
    const defaultLng = -6.642995;
    const zoomLevel = 18;

    const map = initMap(containerId, defaultLat, defaultLng, zoomLevel);
    if (!map) return;

    //Recuperar atributo coordenadas
    const coordenadasDataElement = document.getElementById('coordenadas-data');
    const coordenadasData = coordenadasDataElement ? coordenadasDataElement.getAttribute('coordenadas-data') : null;

    let localizacion = [];
    if (coordenadasData) {
        try {
            localizacion = JSON.parse(coordenadasData);
        } catch (error) {
            console.error("Error al parsear las coordenadas:", error);
        }
    }

    loadGeoJSON(map, localizacion);
});
