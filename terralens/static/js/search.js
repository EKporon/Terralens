/*
=================================
TerraLens Search Handler
=================================
*/


const searchForm = document.getElementById(
    "search-form"
);



if(searchForm){


    searchForm.addEventListener(
        "submit",
        async function(event){


            event.preventDefault();



            const address =
            document.getElementById(
                "address"
            ).value;



            if(!address){

                alert(
                    "Please enter a location."
                );

                return;

            }



            console.log(
                "Searching:",
                address
            );



            /*
            Later this connects to Flask:

            /search?address=value

            */


        }
    );

}
