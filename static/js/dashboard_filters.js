document.addEventListener("DOMContentLoaded", () => {

    const filters = [
        "stateFilter",
        "categoryFilter",
        "arrestFilter"
    ];

    filters.forEach(id => {
        document
            .getElementById(id)
            .addEventListener("change", loadDashboard);
    });

});

async function loadDashboard() {

    const state = document.getElementById("stateFilter").value;
    const category = document.getElementById("categoryFilter").value;
    const arrest = document.getElementById("arrestFilter").value;

    const url = `/api/dashboard?state=${encodeURIComponent(state)}&category=${encodeURIComponent(category)}&arrest=${encodeURIComponent(arrest)}`;

    const response = await fetch(url);

    const data = await response.json();

    document.getElementById("totalCrimes").textContent =
        data.total_crimes;

    document.getElementById("totalStates").textContent =
        data.total_states;

    document.getElementById("totalDistricts").textContent =
        data.total_districts;

    document.getElementById("totalLoss").textContent =
        "₹ " + Number(data.total_loss).toLocaleString("en-IN");

}