document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("filtroForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Evita que la página se recargue

        let formData = new FormData(this);
        let params = new URLSearchParams(formData);

        fetch(this.action + "?" + params.toString(), {
            method: "GET"
        })
        .then(response => response.text())
        .then(data => {
            let parser = new DOMParser();
            let doc = parser.parseFromString(data, "text/html");
            let newContent = doc.getElementById("publicidades-container").innerHTML;
            document.getElementById("publicidades-container").innerHTML = newContent;
        });
    });
});
