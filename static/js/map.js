let map;
let markers;

document.addEventListener("DOMContentLoaded", loadMap);

async function loadMap() {

    map = L.map("crimeMap").setView([22.9734, 78.6569], 5);

    L.tileLayer(
        "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        {
            maxZoom: 18,
            attribution: "&copy; OpenStreetMap"
        }
    ).addTo(map);

    markers = L.markerClusterGroup();

    const response = await fetch("/api/crime-map");

    const crimes = await response.json();

    crimes.forEach(crime => {

        if (!crime.lat || !crime.lng)
            return;

        const marker = L.marker([crime.lat, crime.lng]);

        marker.bindPopup(`
            <b>${crime.category}</b><br>
            <strong>Crime ID:</strong> ${crime.crime_id}<br>
            <strong>State:</strong> ${crime.state}<br>
            <strong>District:</strong> ${crime.district}
        `);

        markers.addLayer(marker);

    });

    map.addLayer(markers);

}