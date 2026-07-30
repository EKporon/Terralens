"""
Input validation utilities.
"""


def validate_coordinates(
    latitude,
    longitude
):


    if not latitude or not longitude:

        return False



    if latitude < -90 or latitude > 90:

        return False



    if longitude < -180 or longitude > 180:

        return False



    return True
