/*
=================================
TerraLens Report Renderer
=================================
*/



document.addEventListener(

"DOMContentLoaded",

()=>{


const stored =
localStorage.getItem(
"terralens_result"
);



if(!stored){

    return;

}



const data =
JSON.parse(
stored
);





document.getElementById(
"location"
).innerHTML =

data.location.name;





document.getElementById(
"weather"
).innerHTML =

`

Temperature:
${data.weather.temperature} °C

<br>

Humidity:
${data.weather.humidity} %

<br>

Wind:
${data.weather.wind_speed} km/h

`;





document.getElementById(
"elevation"
).innerHTML =

`

${data.elevation.elevation}
meters

`;






document.querySelector(
".score h1"
).innerHTML =

`

${data.report.score}
/
100

`;





document.querySelector(
".score p"
).innerHTML =

data.report.summary;




// Load map

initializeMap();



addMarker(

data.location.latitude,

data.location.longitude

);



}

);
