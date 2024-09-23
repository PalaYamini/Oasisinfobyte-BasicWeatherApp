import requests

# Your OpenWeatherMap API key (replace with your actual API key)
api_key = "cf837ef98b157befed60a0d522c42471"

# Function to get weather data from OpenWeatherMap API
def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Main function to display weather data
def main():
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name)
    
    if weather_data["cod"] == 200:  # If the request was successful
        main_data = weather_data["main"]
        weather_description = weather_data["weather"][0]["description"]
        
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Weather: {weather_description}")
    else:
        print(f"Error: {weather_data['message']}")

if __name__ == "__main__":
    main()
