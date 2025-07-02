document.addEventListener("DOMContentLoaded", function () {
    const municipioInput = document.querySelector("input[name='nombre']");
    const comunidadInput = document.querySelector("select[name='comunidad_autonoma']");
    const provinciaInput = document.querySelector("select[name='provincia']");
    const latitudInput = document.querySelector("input[name='latitud']");
    const longitudInput = document.querySelector("input[name='longitud']");

    const PROVINCIAS_POR_COMUNIDAD = {
        "Andalucía": ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"],
        "Aragón": ["Huesca", "Teruel", "Zaragoza"],
        "Asturias": ["Asturias"],
        "Baleares": ["Islas Baleares"],
        "Canarias": ["Las Palmas", "Santa Cruz de Tenerife"],
        "Cantabria": ["Cantabria"],
        "Castilla-La Mancha": ["Albacete", "Ciudad Real", "Cuenca", "Guadalajara", "Toledo"],
        "Castilla y León": ["Ávila", "Burgos", "León", "Palencia", "Salamanca", "Segovia", "Soria", "Valladolid", "Zamora"],
        "Cataluña": ["Barcelona", "Gerona", "Lérida", "Tarragona"],
        "Ceuta": ["Ceuta"],
        "Extremadura": ["Badajoz", "Cáceres"],
        "Galicia": ["La Coruña", "Lugo", "Orense", "Pontevedra"],
        "Madrid": ["Madrid"],
        "Melilla": ["Melilla"],
        "Murcia": ["Murcia"],
        "Navarra": ["Navarra"],
        "La Rioja": ["La Rioja"],
        "País Vasco": ["Álava", "Guipúzcoa", "Vizcaya"],
        "Valencia": ["Alicante", "Castellón", "Valencia"]
    };

    function actualizarProvincias() {
        const comunidadSeleccionada = comunidadInput.value;
        const provinciaPreseleccionada = provinciaInput.getAttribute("data-selected");
        provinciaInput.innerHTML = "";

        if (comunidadSeleccionada in PROVINCIAS_POR_COMUNIDAD) {
            const provincias = PROVINCIAS_POR_COMUNIDAD[comunidadSeleccionada];

            const optionDefault = document.createElement("option");
            optionDefault.value = "";
            optionDefault.textContent = "Selecciona una provincia";
            provinciaInput.appendChild(optionDefault);

            provincias.forEach(provincia => {
                const option = document.createElement("option");
                option.value = provincia;
                option.textContent = provincia;
                
                if (provincia === provinciaPreseleccionada) {
                    option.selected = true;
                }

                provinciaInput.appendChild(option);
            });
        }
    }

    function obtenerCoordenadas() {
        if (!municipioInput.value || !provinciaInput.value || !comunidadInput.value) {
            latitudInput.value = "";
            longitudInput.value = "";
            return;
        }

        const query = `${municipioInput.value}, ${provinciaInput.value}, ${comunidadInput.value}, España`;
        const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    latitudInput.value = data[0].lat;
                    longitudInput.value = data[0].lon;
                } else {
                    latitudInput.value = "";
                    longitudInput.value = "";
                    alert("No se encontraron coordenadas para la dirección proporcionada");
                }
            })
            .catch(error => {
                latitudInput.value = "";
                longitudInput.value = "";
                console.error("Error obteniendo coordenadas:", error);
            });
    }
    
    comunidadInput.addEventListener("change", actualizarProvincias);
    municipioInput?.addEventListener("blur", obtenerCoordenadas);
    provinciaInput?.addEventListener("blur", obtenerCoordenadas);
    comunidadInput?.addEventListener("blur", obtenerCoordenadas);

    actualizarProvincias();
});
