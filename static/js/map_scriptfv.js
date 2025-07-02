document.addEventListener("DOMContentLoaded", function () {
    const mapData = document.getElementById("map-data");
    const latitud = parseFloat(mapData.getAttribute("data-latitud"));
    const longitud = parseFloat(mapData.getAttribute("data-longitud"));

    const map = L.map('map').setView([latitud, longitud], 18);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    const parcelas = JSON.parse(mapData.getAttribute("data-parcelas"));
    const todasParcelas = JSON.parse(mapData.getAttribute("data-parcelas-todas"));
    const idFiesta = mapData.getAttribute("data-id-fiesta");
    let addingParcelas = false; //control de estado que cambia el comportamiento del clic sobre parcelas (añadir vs redirigir)

    function agregarParcelaFiesta(parcelaId) {
        fetch(`/ayuntamiento/fiesta/${idFiesta}/añadir/${parcelaId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert("Error al añadir la parcela");
            }
        })
        .catch(error => console.error("Error:", error));
    }

    function redirigirAParcela(parcelaId) {
        window.location.href = `/parcela/${parcelaId}/${idFiesta}`;
    }

    function mostrarParcelas(parcelasMostrar) {
        parcelasMostrar.forEach(parcela => {
            if (parcela.localizacion) {
                let localizacion = parcela.localizacion;

                if (localizacion && Array.isArray(localizacion[0])) {
                    let parcelCoordinates = {
                        "type": "FeatureCollection",
                        "features": [
                            {
                                "type": "Feature",
                                "geometry": {
                                    "type": "Polygon",
                                    "coordinates": localizacion
                                },
                                "properties": {
                                    "name": parcela.nombre,
                                    "descripcion": parcela.detalles
                                }
                            }
                        ]
                    };

                    if (parcelCoordinates.features[0].geometry.coordinates.length > 0) {
                        const geoJsonLayer = L.geoJSON(parcelCoordinates, {
                            style: function () {
                                return { 
                                    color: parcela.en_fiesta ? 'black' : 'green', 
                                    fillColor: parcela.en_fiesta ? 'black' : 'green', 
                                    fillOpacity: 0.5 
                                };
                            },
                            onEachFeature: function (feature, layer) {
                                layer.bindTooltip(parcela.nombre + ", " + parcela.detalles, { permanent: false, direction: 'top' });

                                layer.on('click', function () {
                                    map.fitBounds(layer.getBounds());
                                    if (addingParcelas) {
                                        if (!parcela.en_fiesta) {
                                            if (confirm(`¿Añadir la parcela "${parcela.nombre}" a la fiesta?`)) {
                                                agregarParcelaFiesta(parcela.id);
                                            }
                                        }
                                    } else {
                                        redirigirAParcela(parcela.id);
                                    }
                                });
                            }
                        }).addTo(map);
                        map.fitBounds(geoJsonLayer.getBounds());
                    }  
                }
            }
        });
    }

    mostrarParcelas(parcelas);

    const parcelalistBtn = document.getElementById("parcelalist");
    const cancelarAñadirBtn = document.getElementById("cancelarAñadir");
    const buscarParcelaInput = document.getElementById("buscarParcela");
    const seleccionarTodasCheckbox = document.getElementById("seleccionarTodas");
    const seleccionarTodasRemoverCheckbox = document.getElementById("seleccionarTodasRemover");
    const añadirParcelasBtn = document.getElementById("añadirParcelasSeleccionadas");

    if (parcelalistBtn) {
        parcelalistBtn.addEventListener("click", function () {
        addingParcelas = true;
        mostrarParcelas(todasParcelas);
        });
    }

    document.querySelectorAll(".parcela-item").forEach(item => {
        item.addEventListener("click", function () {
            const lat = parseFloat(this.dataset.lat);
            const lng = parseFloat(this.dataset.lng);
            if (!isNaN(lat) && !isNaN(lng)) {
                map.setView([lat, lng], 19);
            }
        });
    });

    if (parcelalistBtn) {
        document.getElementById("parcelalist").addEventListener("click", function () {
            document.getElementById("parcelasModal").style.display = "block";
            document.querySelectorAll(".parcela-checkbox").forEach(cb => cb.checked = false);
            document.getElementById("seleccionarTodas").checked = false;
        });
    }
    if (cancelarAñadirBtn) {
        cancelarAñadirBtn.addEventListener("click", function () {
            document.getElementById("parcelasModal").style.display = "none";
            document.querySelectorAll(".parcela-checkbox").forEach(cb => cb.checked = false);
            document.getElementById("seleccionarTodas").checked = false;
        });
    }

    if (buscarParcelaInput) {
        buscarParcelaInput.addEventListener("input", function () {
            let filtro = this.value.toLowerCase();
            document.querySelectorAll("#listaParcelas li").forEach(function (item) {
                let nombre = item.textContent.toLowerCase();
                item.style.display = nombre.includes(filtro) ? "" : "none";
            });
        });
    }

    if (seleccionarTodasCheckbox) {
        seleccionarTodasCheckbox.addEventListener("change", function () {
            let checkboxes = document.querySelectorAll(".parcela-checkbox");
            checkboxes.forEach(cb => cb.checked = this.checked);
        });
    }

    document.querySelectorAll(".parcela-checkbox").forEach(cb => {
        cb.addEventListener("change", function () {
            if (!this.checked) {
                seleccionarTodasCheckbox.checked = false;
            } else {
                let todasMarcadas = [...document.querySelectorAll(".parcela-checkbox")].every(cb => cb.checked);
                seleccionarTodasCheckbox.checked = todasMarcadas;
            }
        });
    });

    if (añadirParcelasBtn) {
        añadirParcelasBtn.addEventListener("click", async function () {
            let seleccionadas = Array.from(document.querySelectorAll(".parcela-checkbox:checked")).map(cb => cb.dataset.id);
            if (seleccionadas.length > 0) {
                for (let parcelaId of seleccionadas) {
                    try {
                        const response = await fetch(`/ayuntamiento/fiesta/${idFiesta}/añadir/${parcelaId}`, {
                        method: 'POST', headers: { 'Content-Type': 'application/json' }
                    });
    
                    if (!response.ok) {
                        console.error(`Error al añadir parcela ${parcelaId}: ${response.statusText}`);
                    }
                    } catch (error) {
                        console.error(`Error en la solicitud de adición:`, error);
                    }
                }
                location.reload();
            }
            document.getElementById("parcelasModal").style.display = "none";
        });
    }
    

    document.getElementById("parcelasRemover").addEventListener("click", function () {
        document.getElementById("parcelasModalRemover").style.display = "block";
        document.querySelectorAll(".parcela-checkbox").forEach(cb => cb.checked = false);
        document.getElementById("seleccionarTodasRemover").checked = false;
    });

    document.getElementById("cancelarQuitar").addEventListener("click", function () {
        document.getElementById("parcelasModalRemover").style.display = "none";
        document.querySelectorAll("#listaParcelasRemover .parcela-checkbox").forEach(cb => cb.checked = false);
        document.getElementById("seleccionarTodasRemover").checked = false;
    });

    document.getElementById("buscarParcelaRemover").addEventListener("input", function () {
        let filtro = this.value.toLowerCase();
        document.querySelectorAll("#listaParcelasRemover li").forEach(function (item) {
            let nombre = item.textContent.toLowerCase();
            item.style.display = nombre.includes(filtro) ? "" : "none";
        });
    });

    document.getElementById("seleccionarTodasRemover").addEventListener("change", function () {
        let checkboxes = document.querySelectorAll("#listaParcelasRemover .parcela-checkbox");
        checkboxes.forEach(cb => cb.checked = this.checked);
    });

    document.querySelectorAll("#listaParcelasRemover .parcela-checkbox").forEach(cb => {
        cb.addEventListener("change", function () {
            if (!this.checked) {
                seleccionarTodasRemoverCheckbox.checked = false;
            } else {
                let todasMarcadas = [...document.querySelectorAll("#listaParcelasRemover .parcela-checkbox")].every(cb => cb.checked);
                seleccionarTodasRemoverCheckbox.checked = todasMarcadas;
            }
        });
    });

    document.getElementById("quitarParcelasSeleccionadas").addEventListener("click", async function () {
        let seleccionadas = Array.from(document.querySelectorAll("#listaParcelasRemover .parcela-checkbox:checked")).map(cb => cb.dataset.id);

        if (seleccionadas.length > 0) {
            for (let parcelaId of seleccionadas) {
                try {
                    const response = await fetch(`/ayuntamiento/fiesta/quitar/${parcelaId}/${idFiesta}`, {
                        method: 'POST', headers: { 'Content-Type': 'application/json' }
                    });
    
                    if (!response.ok) {
                        console.error(`Error al eliminar parcela ${parcelaId}: ${response.statusText}`);
                    }
                } catch (error) {
                    console.error(`Error en la solicitud de eliminación:`, error);
                }
            }
            location.reload();
        }
        document.getElementById("parcelasModalRemover").style.display = "none";
    });
});
