import requests

# OpenWeatherMap API key
API_KEY = '7bd7e1ee73ea64b19afb8c9963a0c483'

def get_weather(city):
    # API URL for current weather
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    # Fetch weather data
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Failed to fetch weather data")
        return

    # Extract relevant information
    weather_data = {
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description'],
        "city": data['name']
    }
    
    print("Weather in", city)
    print("Temperature:", weather_data["temperature"], "°C")
    print("Description:", weather_data["description"])

if __name__ == '__main__':
    city = input("Enter city name: ")
    get_weather(city)
