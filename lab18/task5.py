import requests
import json
import os

def display_weather(city_name):
    api_key = "f698bb0d4fca00919e1bbc3ebf8ad41e"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") == 200:
            city = data.get("name")
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()

            result = {
                "city": city,
                "temp": temp,
                "humidity": humidity,
                "weather": description
            }

            # Display formatted JSON output
            print(json.dumps(result, indent=4))

            # Append to results.json
            filename = "results.json"
            if os.path.exists(filename):
                with open(filename, "r+", encoding="utf-8") as file:
                    try:
                        existing_data = json.load(file)
                    except json.JSONDecodeError:
                        existing_data = []
                    existing_data.append(result)
                    file.seek(0)
                    json.dump(existing_data, file, indent=4)
            else:
                with open(filename, "w", encoding="utf-8") as file:
                    json.dump([result], file, indent=4)

        else:
            print("Error: City not found. Please enter a valid city.")

    except requests.exceptions.HTTPError:
        print("Error: City not found. Please enter a valid city.")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.RequestException:
        print("An error occurred while fetching weather data.")
    except (KeyError, TypeError):
        print("Unexpected response format. Could not extract weather details.")

# Example usage
display_weather("London")
display_weather("New York")
display_weather("warangal")
display_weather("xyz123")
display_weather("Tokyo")
display_weather("Sydney")
display_weather("Mumbai")
