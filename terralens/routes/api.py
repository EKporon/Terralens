"""
TerraLens API Routes
"""


from flask import Blueprint, request, jsonify



from services.geocoder import (
    geocode_address
)


from services.weather import (
    get_weather
)


from services.elevation import (
    get_elevation
)


from services.report import (
    generate_report
)




api_bp = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)




@api_bp.route(
    "/analyze",
    methods=["POST"]
)
def analyze():


    data = request.json



    address = data.get(
        "address"
    )



    if not address:

        return jsonify({

            "error":
            "Address required"

        }), 400




    location = geocode_address(
        address
    )



    if not location:


        return jsonify({

            "error":
            "Location not found"

        }), 404




    latitude = location["latitude"]

    longitude = location["longitude"]




    weather = get_weather(

        latitude,

        longitude

    )



    elevation = get_elevation(

        latitude,

        longitude

    )



    report = generate_report(

        weather,

        elevation

    )




    return jsonify({

        "location":
        location,


        "weather":
        weather,


        "elevation":
        elevation,


        "report":
        report

    })
