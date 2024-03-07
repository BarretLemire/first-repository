import requests

class WeatherAPI:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.weather_data = None
    
    def fetch_weather_data(self):
        url = f"https://api.weather.gov/points/{self.latitude},{self.longitude}"
        response = requests.get(url)
        self.weather_data = response.json()
    
    def get_current_temperature(self):
        if self.weather_data:
            forecast_url = self.weather_data["properties"]["forecastHourly"]
            response = requests.get(url=forecast_url)
            forecast = response.json()
            current_period = forecast["properties"]["periods"][0]
            return current_period["temperature"]
        else:
            return None
    
    def get_current_wind_speed(self):
        if self.weather_data:
            forecast_url = self.weather_data["properties"]["forecastHourly"]
            response = requests.get(url=forecast_url)
            forecast = response.json()
            current_period = forecast["properties"]["periods"][0]
            return current_period["windSpeed"]
        else:
            return None
    
    def get_current_weather_condition(self):
        if self.weather_data:
            forecast_url = self.weather_data["properties"]["forecastHourly"]
            response = requests.get(url=forecast_url)
            forecast = response.json()
            current_period = forecast["properties"]["periods"][0]
            return current_period["shortForecast"]
        else:
            return None


def dress_appropriately(current_temperature, current_wind_speed, weather_condition) -> str:
    if 50 < current_temperature < 60:
        print("You can wear a hoodie or light jacket.")
    
    elif current_wind_speed > 30:
        print("Watch out for tumbleweeds on the roads.")
    
    elif "rain" in weather_condition.lower():
        print("Bring a rain jacket.")
    
    elif current_temperature > 70 and "sunny" in weather_condition.lower():
        print("Wear shorts.")
    
    elif current_temperature < 50:
        print("Layer up, it's cold.")
    
    else:
        print("Weather conditions are moderate, dress as per your comfort.")

if __name__ == "__main__":
    latitude = 37.09859467433797
    longitude = -113.59142241349349
    
    weather_api = WeatherAPI(latitude, longitude)
    weather_api.fetch_weather_data()
    current_temperature = weather_api.get_current_temperature()
    current_wind_speed = weather_api.get_current_wind_speed()
    current_weather_condition = weather_api.get_current_weather_condition()
    
    print("Current Temperature:", current_temperature)
    print("Current Wind Speed:", current_wind_speed)
    print("Current Weather Condition:", current_weather_condition)

suggestion = dress_appropriately(current_temperature, current_wind_speed, current_weather_condition)
print(suggestion)


