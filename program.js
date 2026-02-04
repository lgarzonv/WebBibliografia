var map = L.map('map').setView([4.642365566284839, -74.15616023510594], 17);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var marker = L.marker([4.642365566284839, -74.15616023510594]).addTo(map);