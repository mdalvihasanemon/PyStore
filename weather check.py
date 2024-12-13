import requests

def get_weather(city, api_key="your_openweathermap_api_key"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        print(f"Weather in {city}: {weather['weather'][0]['description']}")
        print(f"Temperature: {weather['main']['temp']}°C")
    else:
        print("City not found or invalid API key.")

get_weather("London")
