import requests
import json
from weather import WeatherFetcher # Importing class from weather.py

def load_api_key() -> str:
    with open('src/config.json', 'r') as file:
        config = json.load(file) # Load JSON data into a dictionary

    return config["API_WEATHER_KEY"] # Return api key

def print_data(response, info):
    fahrenheit = ((info.get("temperature") * (9/5)) +  32)
    if response.status_code == 200:
        print(f"Success!\ncity: ", info.get("city"), "\ncountry: ", info.get("country"), "\ntemp: ", fahrenheit, "\nhumidity: ", info.get("humidity"), "\nwind speed: ", info.get("wind_speed"), "\nweather conditions: ", info.get("weather conditions"), "\ntimezone: ", info.get("timezone"))
    else:
        print("Error: Could not retrieve data.")

def main():
    city = input("What city do you want to check the weather for? ")
    weather = WeatherFetcher(load_api_key())
    url = weather.get_weather_url(city)

    response = requests.get(url)
    data = response.json()

    data_str = str(data)
    with open('src/weather_data.txt', 'w') as file:
        file.write(data_str)

    info = {"city" : data["name"],
        "country" : data["sys"]["country"],
        "temperature" : data["main"]["temp"],
        "humidity" : data["main"]["humidity"],
        "wind_speed" : data["wind"]["speed"], 
        "weather conditions" : data["weather"][0]["description"],
        "timezone" : data["timezone"]
       }

    print_data(response, info)

if __name__ == "__main__": # Telling Python which function to execute first when the script is run directly
    main()