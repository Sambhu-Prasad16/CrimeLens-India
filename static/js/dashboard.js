async function loadRecentCrimes() {

    try {

        const response = await fetch("/api/recent-crimes");
        const data = await response.json();

        // Destroy existing DataTable
        if ($.fn.DataTable.isDataTable("#crimeTable")) {
            $("#crimeTable").DataTable().destroy();
        }

        const tbody = document.querySelector("#crimeTable tbody");
        tbody.innerHTML = "";

        data.forEach(crime => {

            tbody.innerHTML += `
                <tr>
                    <td>${crime.crime_id}</td>
                    <td>${crime.date}</td>
                    <td>${crime.state}</td>
                    <td>${crime.district}</td>
                    <td>${crime.category}</td>
                    <td>${crime.arrest}</td>
                    <td>₹ ${Number(crime.loss).toLocaleString("en-IN")}</td>
                </tr>
            `;

        });

        new DataTable("#crimeTable", {

            pageLength: 10,

            responsive: true,

            ordering: true,

            searching: true,

            lengthChange: true,

            info: true,

            layout: {

                topStart: {

                    buttons: ["copy", "csv", "excel", "print"]

                }

            }

        });

    } catch (error) {

        console.error("Error loading crime table:", error);

    }

}

document.addEventListener("DOMContentLoaded", function () {

    loadRecentCrimes();

});