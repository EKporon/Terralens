/*
=================================
TerraLens Search Controller
=================================
*/


const form = document.getElementById(
    "search-form"
);



if(form){


form.addEventListener(
"submit",
async function(event){


event.preventDefault();



const address =
document.getElementById(
"address"
).value;



if(!address){

    alert(
    "Please enter an address"
    );

    return;

}




try{


const response =
await fetch(
"/api/analyze",
{

method:"POST",

headers:
{

"Content-Type":
"application/json"

},

body:
JSON.stringify(
{
address: address
}
)

}

);




const data =
await response.json();



if(data.error){

    alert(data.error);

    return;

}




// Save result temporarily

localStorage.setItem(

"terralens_result",

JSON.stringify(data)

);




// Go to dashboard

window.location.href =
"/results";





}

catch(error){


console.error(
error
);


alert(
"Unable to analyze location."
);


}



});

}
