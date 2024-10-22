import tkinter as tk
from tkinter import messagebox
import requests
import pandas as pd
import numpy as np

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.resizable(0, 0)
        self.root.title("Weather App")

        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.api_key = # Repalce your API key

        self.create_widgets()

    def create_widgets(self):
        self.city_label = tk.Label(self.root, text="Enter City Name:", font=("Times New Roman", 12, "normal"))
        self.city_label.pack(pady=10)
        self.city_entry = tk.Entry(self.root, width=24, font=("Times New Roman", 14, "normal"))
        self.city_entry.pack()

        self.output_label = tk.Label(self.root, text="", font=("Times New Roman", 12))
        self.output_label.pack(pady=20)

        self.check_button = tk.Button(self.root, text="Check Weather", font=("Times New Roman", 10),
                                      command=self.get_weather, bg="black", fg="Aqua", padx=5, pady=5)
        self.check_button.pack(pady=20)

    def get_weather(self):
        city_name = self.city_entry.get()

        if not city_name:
            messagebox.showwarning("Warning", "Please enter a city name.")
            return

        try:
            complete_url = f"{self.base_url}appid={self.api_key}&q={city_name}"
            response = requests.get(complete_url)
            data = response.json()
            if data.get("cod") == 200:
                self.display_weather_data(data)
            else:
                messagebox.showerror("Error", f"City not found or error in API response. Response code: {data.get('cod')}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to retrieve data from the API. {e}")

    def display_weather_data(self, data):
        main_data = data.get("main")
        wind_data = data.get("wind")
        weather_data = data.get("weather", [])[0]

        if main_data and wind_data and weather_data:
            temperature_kelvin = main_data.get("temp")
            atmospheric_pressure = main_data.get("pressure")
            humidity = main_data.get("humidity")
            description = weather_data.get("description")
            wind_speed = wind_data.get("speed")
            wind_degree = wind_data.get("deg")

            temperature_celsius = self.kelvin_to_celsius(temperature_kelvin)

            weather_df = pd.DataFrame({
                "Parameter": ["Temperature (°C)", "Atmospheric Pressure (hPa)", "Humidity (%)", "Description",
                              "Wind Speed (m/s)", "Wind Direction (°)"],
                "Value": [f"{temperature_celsius:.1f}", f"{atmospheric_pressure}", f"{humidity}", description,
                          f"{wind_speed}", f"{wind_degree}"]
            })

            self.output_label.config(text=weather_df.to_string(index=False, header=False), fg="blue")
        else:
            messagebox.showerror("Error", "Incomplete or missing data in the API response.")

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
