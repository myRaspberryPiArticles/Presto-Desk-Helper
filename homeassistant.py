# Home Assistant API interface for distance & time variables

import secrets
import requests

# Add your HA long-lived access token to secrets.py in the Presto
secrets.require("HA_KEY")
HA_KEY = secrets.HA_KEY
headers = {"Authorization": f"Bearer {HA_KEY}", "Content-Type": "application/json"}

# Entity IDs for distance and time input numbers
DISTANCE_ENTITY = "input_number.distance_rowed"
TIME_ENTITY = "input_number.time_rowed"

# Home Assistant base url
BASE_URL = "http://homeassistant.local:8123"

# fetches the distance & time from Home Assistant
# Returns 2 values - distance and time
def fetch_data():
    distance_request = requests.get(
        f"{BASE_URL}/api/states/{DISTANCE_ENTITY}",
        headers=headers,
    )

    distance = distance_request.json()["state"]

    time_request = requests.get(
        f"{BASE_URL}/api/states/{TIME_ENTITY}",
        headers=headers,
    )

    time = time_request.json()["state"]

    return distance, time

# Updates the state of the distance entity in Home Assistant
# Returns the HTTP status code of the POST
def update_distance(value):
    data = {"state": value}

    request = requests.post(
        f"{BASE_URL}/api/states/{DISTANCE_ENTITY}",
        headers=headers,
        data=data
    )

    return request.status_code

# Updates the state of the time entity in Home Assistant
# Returns the HTTP status code of the POST
def update_time(value):
    data = {"state": value}

    request = requests.post(
        f"{BASE_URL}/api/states/{TIME_ENTITY}",
        headers=headers,
        data=data
    )

    return request.status_code
