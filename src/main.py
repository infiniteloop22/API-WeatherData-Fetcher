import requests
import json
from weather import WeatherFetcher # Importing class from weather.py

def load_api_key() -> str:
    with open('.\src\config.json', 'r') as file:
        config = json.load(file) # Load JSON data into a dictionary

    return config["API_WEATHER_KEY"] # Return api key

def print_data(response, info):
    if response.status_code == 200:
        print(f"Success!\ncity: ", info.get("city"), "\ntemp: ", info.get("temperature"), "\nweather conditions: ", info.get("weather conditions"))
        #print(data) # viewing json data as a dictionary
    else:
        print("Error: Could not retrieve data.")

def main():
    city = input("What city do you want to check the weather for? ")
    weather = WeatherFetcher(load_api_key())
    url = weather.get_weather_url(city)

    response = requests.get(url)
    data = response.json()

    info = {"city" : data["name"],
        "temperature" : data["main"]["temp"], 
        "weather conditions" : data["weather"][0]["description"]
       }

    print_data(response, info)

if __name__ == "__main__": # Telling Python which function to execute first when the script is run directly
    main()