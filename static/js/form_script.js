document.addEventListener('DOMContentLoaded', function () {
    const roleField = document.querySelector('select[name="rol"]');
    const ayuntamientoFields = document.getElementById('ayuntamiento-fields');
    const ferianteFields = document.getElementById('feriante-fields');

    function toggleFields() {
        const selectedRole = roleField.value;
        ayuntamientoFields.style.display = selectedRole === 'ayuntamiento' ? 'block' : 'none';
        ferianteFields.style.display = selectedRole === 'feriante' ? 'block' : 'none';
    }

    roleField.addEventListener('change', toggleFields);
    toggleFields(); //Muestra/oculta dinámicamente secciones del formulario en función del rol elegido

    const telefonoInput = document.querySelector("input[name='tlf']");

    if (telefonoInput) {
        telefonoInput.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, "");

            if (this.value.length > 9) {
                this.value = this.value.slice(0, 9);
            }
        });

        document.querySelector("form").addEventListener("submit", function (event) {
            if (telefonoInput.value.length !== 9) {
                event.preventDefault();
                alert("El teléfono debe tener exactamente 9 dígitos.");
            }
        });
    }
});
