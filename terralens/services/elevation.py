"""
TerraLens Elevation Service
"""


import requests

from config import Config



def get_elevation(latitude, longitude):


    payload = {


        "locations":

        [

            {

                "latitude":
                latitude,


                "longitude":
                longitude

            }

        ]

    }



    response = requests.post(

        Config.ELEVATION_URL,

        json=payload

    )



    data = response.json()



    if "results" not in data:

        return None



    return {


        "elevation":

        data["results"][0]["elevation"]

    }
