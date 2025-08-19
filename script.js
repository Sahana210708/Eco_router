// Initialize Leaflet map
var mapElement = document.getElementById("map");
if (mapElement) {
    var map = L.map('map').setView([13.0827, 80.2707], 10); // Chennai

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);
}

// Navigate to other pages
function navigateTo(page) {
    window.location.href = page;
}
