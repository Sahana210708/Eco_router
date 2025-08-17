// Initialize map
var map = L.map('map').setView([13.0827, 80.2707], 10); // Centered on Chennai

// Add tile layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to load database data
function loadData(collectionName) {
    fetch(`http://127.0.0.1:5000/${collectionName}`)
        .then(response => response.json())
        .then(data => {
            const output = document.getElementById("output");
            output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;

            // Example: If collection has locations, show on map
            map.eachLayer(function(layer) {
                if (layer instanceof L.Marker) {
                    map.removeLayer(layer);
                }
            });

            data.forEach(item => {
                if (item.lat && item.lng) {
                    L.marker([item.lat, item.lng]).addTo(map)
                      .bindPopup(`<b>${collectionName}</b><br>${JSON.stringify(item)}`);
                }
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
}
