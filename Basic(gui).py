import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    city_name = city_entry.get()

    if not city_name:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return

    try:
        complete_url = f"{base_url}appid={api_key}&q={city_name}"
        response = requests.get(complete_url)
        data = response.json()

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

                # Determine umbrella type based on wind direction
                if wind_degree <= 22.5 or wind_degree > 337.5:
                    umbrella_type = "Full"
                elif wind_degree <= 67.5:
                    umbrella_type = "Compact"
                elif wind_degree <= 112.5:
                    umbrella_type = "Small"
                elif wind_degree <= 157.5:
                    umbrella_type = "Bubble"
                elif wind_degree <= 202.5:
                    umbrella_type = "Classic"
                elif wind_degree <= 247.5:
                    umbrella_type = "Beach"
                elif wind_degree <= 292.5:
                    umbrella_type = "Sport"
                else:
                    umbrella_type = "Full"

                # Check if output_label exists
                if not hasattr(get_weather, 'output_label'):
                    # Output label doesn't exist, create it
                    get_weather.output_label = tk.Label(root, text="", font=("Arial", 12))
                    get_weather.output_label.pack(pady=20)

                # Configure output_label with weather information and umbrella type
                get_weather.output_label.config(
                    text=f"Temperature: {temperature:.1f}°C\nAtmospheric Pressure: {atmospheric_pressure} hPa\nHumidity: {humidity}%\nDescription: {description}\nWind Speed: {wind_speed} m/s\nWind Direction: {wind_degree}°\nUmbrella Type: {umbrella_type}",
                    fg="Blue")

            else:
                messagebox.showerror("Error", "Incomplete or missing data in the API response.")
        else:
            messagebox.showerror("Error", f"City not found or error in API response. Response code: {data.get('cod')}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data from the API. {e}")

# Initialize window
root = tk.Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Weather App")

# City name label and entry
city_label = tk.Label(root, text="Enter City Name:", font=("Times New Roman", 12, "normal"))
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=24, font=("Times New Roman", 14, "normal"))
city_entry.pack()

# API key and URL
api_key = # Repalce your API key
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Output label
output_label = tk.Label(root, text="", font=("Times New Roman", 12))
output_label.pack(pady=20)

# Check weather button
check_button = tk.Button(root, text="Check Weather", font=("Times New Roman", 10), command=get_weather, bg="black",
                         fg="Aqua", activebackground="teal", padx=5, pady=5)
check_button.pack(pady=20)

root.mainloop()
