import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    data = response.json()

    print("API Response:", data)

    if data.get("cod") == 200:
        main_data = data.get("main")
        wind_data = data.get("wind")
        weather_data = data.get("weather", [])[0]

        if main_data and wind_data and weather_data:
            temperature = main_data.get("temp") - 273.15
            atmospheric_pressure = main_data.get("pressure")
            humidity = main_data.get("humidity")
            description = weather_data.get("description")
            wind_speed = wind_data.get("speed")
            wind_degree = wind_data.get("deg")

            print(f"Temperature: {temperature:.1f}°C")
            print(f"Atmospheric Pressure: {atmospheric_pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description}")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Wind Direction: {wind_degree}°")
            if wind_degree <= 22.5 or wind_degree > 337.5:
                print("Umbrella Type: Full")
            elif wind_degree <= 67.5:
                print("Umbrella Type: Compact")
            elif wind_degree <= 112.5:
                print("Umbrella Type: Small")
            elif wind_degree <= 157.5:
                print("Umbrella Type: Bubble")
            elif wind_degree <= 202.5:
                print("Umbrella Type: Classic")
            elif wind_degree <= 247.5:
                print("Umbrella Type: Beach")
            elif wind_degree <= 292.5:
                print("Umbrella Type: Sport")
            else:
                print("Umbrella Type: Full")
            # else:
            # print("City not found")



        else:
            print("Incomplete or missing data in the API response.")
    else:
        print(f"City not found or error in API response. Response code: {data.get('cod')}")

if __name__ == "__main__":
    city = input("Enter the Name of City: ")
    api_key = # Repalce your API key
    get_weather(city, api_key)
