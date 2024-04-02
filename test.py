
import requests
from tkinter import *
import math

city_name = "Seattle,US"

api_key = "dc29dd7620180a272f294ca0da04c467"

## making the weather call function

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    ## fetching the api request in the json format
    response = requests.get(url).json()
    print(response)

    temp = response['main']['feels_like']
    temp = math.floor((temp * 1.8) - 459.67)  #converting kelvin to Farenheit


    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)

    humdity = response['main']['humidity']

    return {
        'temp': temp,
        'feels_like': feels_like,
        'humdity': humdity

    }


weather = get_weather(api_key, city_name)

print(weather['temp'])
print(weather['feels_like'])
print(weather['humdity'])