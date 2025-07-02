document.addEventListener("DOMContentLoaded", function () {
    const cookieBanner = document.getElementById("cookie-banner");
    const acceptAllBtn = document.getElementById("accept-all-cookies");
    const configureBtn = document.getElementById("configure-cookies");
    const saveSettingsBtn = document.getElementById("save-cookie-settings");

    const modalElement = document.getElementById("cookie-settings-modal");
    const modal = new bootstrap.Modal(modalElement);

    //Creo una cookie con nombre, valor y expiración en días. Incluye flags de Secure y SameSite=Lax para mayor seguridad
    function setCookie(name, value, days) {
        let expires = "";
        if (days) {
            let date = new Date();
            date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + value + "; path=/; Secure; SameSite=Lax" + expires;
    }

    function getCookie(name) {
        let nameEQ = name + "=";
        let ca = document.cookie.split(";");
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i].trim();
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    function hideBanner() {
        cookieBanner.classList.add("d-none");
    }

    function showBanner() {
        cookieBanner.classList.remove("d-none");
    }

    if (getCookie("cookiesAccepted") === "true") {
        hideBanner();
    } else {
        showBanner();
    }

    acceptAllBtn.addEventListener("click", function () {
        setCookie("cookiesAccepted", "true", 365);
        setCookie("analyticsCookies", "true", 365);
        setCookie("marketingCookies", "true", 365);
        hideBanner();
    });

    configureBtn.addEventListener("click", function () {
        modal.show();
    });

    saveSettingsBtn.addEventListener("click", function () {
        const analytics = document.getElementById("analytics-cookies").checked;
        const marketing = document.getElementById("marketing-cookies").checked;

        setCookie("cookiesAccepted", "true", 365);
        setCookie("analyticsCookies", analytics ? "true" : "false", 365);
        setCookie("marketingCookies", marketing ? "true" : "false", 365);

        modal.hide();
        hideBanner();
    });
});
