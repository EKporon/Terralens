"""
TerraLens Land Intelligence Report
"""


def generate_report(
    weather,
    elevation
):


    score = 50


    comments = []



    if elevation:


        height = elevation["elevation"]


        if height > 1000:

            score += 20

            comments.append(

                "Moderate elevation suitable for development."

            )


        else:

            comments.append(

                "Low elevation area. Flood analysis recommended."

            )




    if weather:


        temperature = weather["temperature"]


        if 18 <= temperature <= 30:

            score += 20


            comments.append(

                "Favorable climate conditions detected."

            )



        else:

            comments.append(

                "Temperature conditions may require consideration."

            )




    if score > 100:

        score = 100




    return {


        "score":
        score,


        "summary":

        " ".join(comments)

    }
