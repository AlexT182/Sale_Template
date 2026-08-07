/** @odoo-module **/

function initializeElyWorldPage() {
    document.querySelectorAll(".js_ew_scroll_top").forEach((button) => {
        if (button.dataset.ewBound === "1") {
            return;
        }
        button.dataset.ewBound = "1";
        button.addEventListener("click", () => {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    });
}

document.addEventListener("DOMContentLoaded", initializeElyWorldPage);
document.addEventListener("website_page_loaded", initializeElyWorldPage);
