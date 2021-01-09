import requests
from datetime import datetime


# Nutritonix API INFO
nutrionix_app_ID = "#####THIS HAS BEEN CHANGED, GET YOUR OWN"
nutrionix_app_KEYS = "#####THIS HAS BEEN CHANGED, GET YOUR OWN"
nutrionix_app_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# USER INFO
GENDER = "male"
WEIGHT = 100.2
HEIGHT = 175.26
AGE = 23

SHEET_ENDPOINT = "#####THIS HAS BEEN CHANGED, GET YOUR OWN"
SHEETY_TOKEN = "#####THIS HAS BEEN CHANGED, GET YOUR OWN"



headers = {
    "x-app-id" : nutrionix_app_ID,
    "x-app-key": nutrionix_app_KEYS,
}


user_input = input("Enter workout: ")

parameters = {
     "query": user_input,
     "gender": GENDER,
     "weight_kg": WEIGHT,
     "height_cm": HEIGHT,
     "age": AGE
    }

response = requests.post(url=nutrionix_app_ENDPOINT, json=parameters, headers=headers)
data = response.json()

headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for entry in data["exercises"]:
    sheety_parameters = {
        "workout" : {
            "date" : str(datetime.now().date()),
            "time" : str(datetime.now().strftime("%H:%M:%S")),
            "exercise" : entry['name'],
            "duration": entry['duration_min'],
            "calories": entry['nf_calories']

        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=sheety_parameters, headers=headers)
    print(response.text)
