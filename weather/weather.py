import requests



latitude = 37.09859467433797
longitude = -113.59142241349349

url = f"https://api.weather.gov/points/{latitude},{longitude}"


response = requests.get(url=url)
weather_data = response.json()
print(weather_data)

forecast_url = weather_data["properties"]["forecastHourly"]
response = requests.get(url=forecast_url)
forecast = response.json()
print()

periods = forecast["properties"]["periods"]

current_period = periods[0]
current_temperature = current_period["temperature"]
current_wind_speed = current_period["windSpeed"]
weather_condition= current_period["shortForecast"]
print()


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

