document.addEventListener("DOMContentLoaded", async () => {

    const response = await fetch("/api/monthly-crimes");

    const result = await response.json();

    const ctx = document.getElementById("monthlyCrimeChart");

    new Chart(ctx, {

        type: "line",

        data: {

            labels: result.labels,

            datasets: [{

                label: "Number of Crimes",

                data: result.values,

                borderColor: "#0d6efd",

                backgroundColor: "rgba(13,110,253,0.15)",

                borderWidth: 3,

                fill: true,

                tension: 0.35,

                pointRadius: 4

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: true

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

});