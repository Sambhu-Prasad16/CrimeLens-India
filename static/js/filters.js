document.addEventListener("DOMContentLoaded", loadFilters);

async function loadFilters() {

    const response = await fetch("/api/filters");

    const data = await response.json();

    fillSelect("stateFilter", data.states);

    fillSelect("categoryFilter", data.categories);

    fillSelect("arrestFilter", data.arrest_status);

}

function fillSelect(id, items) {

    const select = document.getElementById(id);

    items.forEach(item => {

        const option = document.createElement("option");

        option.value = item;

        option.textContent = item;

        select.appendChild(option);

    });

}