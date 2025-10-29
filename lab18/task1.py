import requests
import json

def display_weather(city_name):
    api_key = "f698bb0d4fca00919e1bbc3ebf8ad41e"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    weather_json = response.json()
    print(json.dumps(weather_json, indent=4))

# Example usage
display_weather("Warangal")