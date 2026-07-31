/*
=================================
TerraLens Map Controller
=================================
*/


let map;



function initializeMap(){



map = L.map(
"map"
)
.setView(

[
-1.9441,
30.0619
],

13

);



L.tileLayer(

"https://tile.openstreetmap.org/{z}/{x}/{y}.png",

{

attribution:
"© OpenStreetMap contributors"

}

)

.addTo(map);



}




function addMarker(
latitude,
longitude
){



L.marker(

[
latitude,
longitude
]

)

.addTo(map);



map.setView(

[
latitude,
longitude
],

15

);



}
