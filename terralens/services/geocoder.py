"""
TerraLens Geocoder Service

Converts user addresses into
latitude and longitude coordinates.
"""


import requests

from config import Config



def geocode_address(address):

    """
    Convert address to coordinates.

    Returns:
        {
            "name": location name,
            "latitude": lat,
            "longitude": lon
        }
    """


    params = {

        "q": address,

        "format": "json",

        "limit": 1

    }



    headers = {

        "User-Agent":
        "TerraLens/1.0"

    }



    response = requests.get(

        Config.NOMINATIM_URL,

        params=params,

        headers=headers

    )



    data = response.json()



    if not data:

        return None



    location = data[0]



    return {


        "name":
        location["display_name"],


        "latitude":
        float(location["lat"]),


        "longitude":
        float(location["lon"])


    }
