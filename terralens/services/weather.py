"""
TerraLens Weather Service

Gets current weather data.
"""


import requests

from config import Config



def get_weather(latitude, longitude):


    params = {


        "latitude":
        latitude,


        "longitude":
        longitude,


        "current":
        "temperature_2m,relative_humidity_2m,wind_speed_10m"


    }



    response = requests.get(

        Config.WEATHER_URL,

        params=params

    )



    data = response.json()



    if "current" not in data:

        return None



    current = data["current"]



    return {


        "temperature":
        current["temperature_2m"],


        "humidity":
        current["relative_humidity_2m"],


        "wind_speed":
        current["wind_speed_10m"]


    }
