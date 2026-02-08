import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ⚠️ Hardcode your API key here
API_KEY = " Your API key here "


# ---------------- Weather Function ----------------
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    # OpenWeather API call
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},PK&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather = data['weather'][0]['description']

        result_label.config(
            text=f"🌍 City: {city}\n"
                 f"🌡 Temperature: {temp}°C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"⏱ Pressure: {pressure} hPa\n"
                 f"☁️ Weather: {weather}"
        )
    else:
        messagebox.showerror("Error", f"City not found: {city}")


# ---------------- Tkinter GUI ----------------
root = tk.Tk()
root.title("Weather App 🌦")

# Window size
root.geometry("800x500")

# ---- Background ----
bg_image = Image.open("background.jpg")   # make sure file exists
bg_image = bg_image.resize((800, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---- Frame for input ----
frame = tk.Frame(root, bg="#222831", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.05, anchor="n")

tk.Label(
    frame,
    text="Enter City (e.g. Islamabad or London,GB):",
    font=("Arial", 12),
    bg="#222831",
    fg="white"
).pack(pady=10)

city_entry = tk.Entry(
    frame,
    font=("Arial", 12),
    width=30,
    bg="#393E46",
    fg="white",
    insertbackground="white"
)
city_entry.pack(pady=5)

tk.Button(
    frame,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather,
    bg="#00ADB5",
    fg="white"
).pack(pady=10)

# ---- Result Box ----
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    justify="left",
    bg="#222831",
    fg="white",
    bd=2,
    relief="solid",
    padx=10,
    pady=10
)
result_label.place(relx=0.5, rely=0.3, anchor="n")

root.mainloop()

