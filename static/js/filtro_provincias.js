document.addEventListener("DOMContentLoaded", function () {
    const provinciasData = JSON.parse(document.getElementById("provincias-data").textContent || "[]");
    
    //Detengo la ejecución si no hay datos válidos, evitando errores posteriores
    if (provinciasData.length === 0) {
        console.warn("No hay provincias disponibles para filtrar");
        return;
    }

    let toggle = document.createElement("div");
    toggle.id = "provincia-toggle";
    toggle.onclick = function () {
        let lista = document.getElementById("provincia-lista");
        if (lista) {
            lista.style.display = "block";
        }
    };

    const filtroForm = document.getElementById("filtroProvinciasForm");
    const provinciaLista = document.getElementById("provincia-lista");
    const limpiarBtn = document.getElementById("limpiarFiltroBtn");
    const checkboxes = document.querySelectorAll("#provincia-lista .form-check-input");

    const listarContainer = document.getElementById("listar");
    if (listarContainer && provinciaLista) {
        listarContainer.insertBefore(toggle, provinciaLista);
        provinciaLista.style.display = "block";
    } else {
        console.error("No hay eventos para ninguna provincia");
    }

    limpiarBtn.addEventListener("click", function () {
        checkboxes.forEach(cb => cb.checked = false);
        document.getElementById("filtroProvinciasForm").submit();
    });
});
