import datetime as dt
import os

import requests


header = {
    'x-app-id': os.environ['app_id'],
    'x-app-key': os.environ['app_key'],
    'x-remote-user-id': '0'
}

activity = input("what activity did you do? ")

parameters = {
    "query": activity,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 23
}

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
response = requests.post(url=nutritionix_endpoint, json=parameters, headers=header).json()

authorization = {
          "Authorization": os.environ['token']
          }
sheet_endpoint = 'https://api.sheety.co/741a2f19f8f8267676dfb4f10758212d/workoutTracker/workouts'

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=authorization)

    print(sheet_response.text)

