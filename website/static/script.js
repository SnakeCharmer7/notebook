document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("themeToggle");
    const currentTheme = localStorage.getItem("theme") || "light";

    document.documentElement.setAttribute("data-bs-theme", currentTheme);
    updateButtonText(currentTheme);

    themeToggle.addEventListener("click", function () {
        const newTheme = document.documentElement.getAttribute("data-bs-theme") === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-bs-theme", newTheme);
        localStorage.setItem("theme", newTheme);
        updateButtonText(newTheme);
    });

    function updateButtonText(theme) {
        themeToggle.textContent = theme === "light" ? "🌙" : "☀️";
    }
});

function closeModal() {
    let modal = document.getElementById('editModal');
    let modalInstance = bootstrap.Modal.getInstance(modal);
    
    if (modalInstance) {
        modalInstance.hide();
    }

    // Usuwamy blokadę scrollowania i backdrop
    document.body.classList.remove('modal-open');
    document.body.style.overflow = "auto";
    document.body.style.paddingRight = "";

    // Usuwamy backdrop (przyciemnienie) w razie potrzeby
    document.querySelectorAll('.modal-backdrop').forEach(backdrop => backdrop.remove());
}

// Dodatkowe zabezpieczenie: usuwamy blokady przy zamknięciu modala
document.addEventListener("hidden.bs.modal", function () {
    document.body.classList.remove("modal-open");
    document.body.style.overflow = "auto";
    document.body.style.paddingRight = "";
});