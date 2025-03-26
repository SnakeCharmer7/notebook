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