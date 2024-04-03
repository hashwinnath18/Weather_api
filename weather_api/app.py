"""from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    # Replace this with actual weather data fetching logic
    weather_data = {
        "temperature": 25,
        "description": "Sunny",
        "city": "New York"
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
"""

"""from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    # Replace this with actual weather data fetching logic
    weather_data = {
        "temperature": 25,
        "description": "Sunny",
        "city": "New York"
    }
    return jsonify(weather_data)

@app.route('/')
def welcome():
    return "Welcome to the Weather API!"

if __name__ == '__main__':
    app.run(debug=True)
    """
    
    
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = '7bd7e1ee73ea64b19afb8c9963a0c483'

@app.route('/weather')
def get_weather():
    # API URL for current weather
    url = f'http://api.openweathermap.org/data/2.5/weather?q=New%20Delhi,IN&appid={API_KEY}&units=metric'
    
    
    # Fetch weather data
    response = requests.get(url)
    data = response.json()

    # Extract relevant information
    weather_data = {
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description'],
        "city": data['name']
    }
    
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)

    
    
    
    