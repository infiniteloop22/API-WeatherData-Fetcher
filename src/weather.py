class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key;

    def get_weather_url(self, city):
        return f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"