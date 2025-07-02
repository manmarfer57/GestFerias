document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');

    if (calendarEl) {
        const eventosFiestas = JSON.parse(document.getElementById("eventos-fiestas-data").textContent);

        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            locale: 'es',
            firstDay: 1,
            themeSystem: 'bootstrap5',
            events: eventosFiestas,
            eventTextColor: 'black',
            buttonText: {
                today: 'Hoy',
                week: 'Semana',
                day: 'Día'
            }
        });

        calendar.render();

    }
});
