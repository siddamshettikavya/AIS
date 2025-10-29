import requests

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

        # Check if city was found
        if data.get("cod") == 200:
            city = data.get("name")
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()

            print(f"City: {city}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description}")
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
display_weather("New York")   # Valid input
display_weather("xyz123")     # Invalid input
display_weather("warangal")
display_weather("London")