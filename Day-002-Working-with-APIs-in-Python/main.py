import requests
from datetime import datetime

# --- 1. ISS API - No Key Needed ---
print("--- 1. ISS Current Location ---")
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_position = data["iss_position"]
print(f"ISS Latitude: {iss_position['latitude']}, Longitude: {iss_position['longitude']}")

# --- 2. Sunrise-Sunset API ---
print("\n--- 2. Sunrise & Sunset Time ---")
MY_LAT = 19.3919  # Virar ka Lat
MY_LONG = 72.8395 # Virar ka Long

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

# --- 3. OpenWeather API (Free Key lagta hai) ---
print("\n--- 3. OpenWeatherMap ---")
# https://openweathermap.org/api se free API key lo
API_KEY = "YOUR_API_KEY_HERE" 
# Agar key nahi hai to isko comment kar do

if API_KEY != "YOUR_API_KEY_HERE":
    weather_params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=weather_params)
    print(response.json())
else:
    print("Add your OpenWeather API key to get real weather data")