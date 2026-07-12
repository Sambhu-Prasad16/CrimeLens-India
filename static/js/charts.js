document.addEventListener("DOMContentLoaded", () => {

    loadMonthlyChart();
    loadStateChart();
    loadCategoryChart();
    loadArrestChart();

});

// ---------------- Monthly ----------------

async function loadMonthlyChart() {

    const response = await fetch("/api/monthly-crimes");
    const data = await response.json();

    new Chart(document.getElementById("monthlyCrimeChart"), {

        type: "line",

        data: {

            labels: data.labels,

            datasets: [{

                label: "Crimes",

                data: data.values,

                borderColor: "#0d6efd",

                backgroundColor: "rgba(13,110,253,0.2)",

                fill: true,

                tension: 0.4

            }]

        }

    });

}

// ---------------- States ----------------

async function loadStateChart() {

    const response = await fetch("/api/top-states");
    const data = await response.json();

    new Chart(document.getElementById("stateChart"), {

        type: "bar",

        data: {

            labels: data.labels,

            datasets: [{

                label: "Crimes",

                data: data.values

            }]

        },

        options: {

            indexAxis: "y"

        }

    });

}

// ---------------- Category ----------------

async function loadCategoryChart() {

    const response = await fetch("/api/crime-categories");
    const data = await response.json();

    new Chart(document.getElementById("categoryChart"), {

        type: "pie",

        data: {

            labels: data.labels,

            datasets: [{

                data: data.values

            }]

        }

    });

}

// ---------------- Arrest ----------------

async function loadArrestChart() {

    const response = await fetch("/api/arrest-status");
    const data = await response.json();

    new Chart(document.getElementById("arrestChart"), {

        type: "doughnut",

        data: {

            labels: data.labels,

            datasets: [{

                data: data.values

            }]

        }

    });

}