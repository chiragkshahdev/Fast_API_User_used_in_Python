# Day 2 - Working with APIs in Python

Second day of API Learning - Handling Parameters, JSON and API Keys.

### 📚 What I Learned
- 'request.get()' with 'params' argument
- 'response.raise_for_status()' for Error Handling
- Parsing JSON data 'response.JSON()'
- Using lat/lng parameters for location APIs
- How API Keys work (OpenWeatherMap)

### 🚀 Projects Covered

**1. ISS Tracker API**
- Endpoint: 'http://api.open-notify.org/iss-now.json'
- No API Key Needed
- Gets current position of International Space Station

**2. Sunrise-Sunset API**
- Endpoint: 'https://api.sunrise-sunset.org/json'
- Uses 'params' - lat, lng, formatted
- Returns sunrise/sunset time for Virar Location

**3. OpenWeatherMap API (Optional)**
- Needs free API Key from openweathermap.org
- Returns Real Temperature

### ▶️ How to Run
'''bash
pip install requests
python main.py