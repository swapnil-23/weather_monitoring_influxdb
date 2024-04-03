
import requests
from tkinter import *
import math

#city_name = "Seattle,US"
city_name = input("Enter your city: ")

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

    humidity = response['main']['humidity']

    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity

    }


weather = get_weather(api_key, city_name)

## making the tkinter gui

root = Tk()
root.geometry("300x300")
root.title(f'{city_name[:-3]} Weather')

## making the title 

def display_city_name(city):
    city_label = Label(root, text=f"{city_name[:-3]}")
    city_label.config(font=("Times New Roman", 28))
    city_label.pack(side='top')


## making the weather stats field
    
def display_stats(weather):
    temp = Label(root, text=f"Temperature: {weather['temp']} F")
    feels_like = Label(root, text=f"Feels Like: {weather['feels_like']} F")
    humidity = Label(root, text=f"Humidity: {weather['humidity']} %")


    temp.config(font=("Arial", 22))
    feels_like.config(font=("Arial", 16))
    humidity.config(font=("Arial", 16))

    temp.pack(side='top')
    feels_like.pack(side='top')
    humidity.pack(side='top')


display_city_name(city_name)

display_stats(weather)

mainloop()