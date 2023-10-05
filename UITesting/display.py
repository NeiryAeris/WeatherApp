from tkinter import *
import tkinter.messagebox
import datetime
import json
from io import BytesIO
from PIL import Image, ImageTk
import requests

file_name = "testing_data.json"


def read_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def display_daily_weather():
    weather = read_data(file_name)
    daily_weather = weather["daily"]
    if daily_weather:
        daily_text_box.delete(1.0, END)
        for entry in daily_weather:
            time = str(datetime.datetime.fromtimestamp(entry["dt"]))
            daily_text_box.insert(
                END,
                f"{time[5:]}: {entry['temp']}°K, {entry['weather'][0]['description']}\n",
            )
    else:
        daily_text_box.delete(1.0, END)
        daily_text_box.insert(END, "File not found or invalid JSON data.")


def display_hourly_weather():
    weather = read_data(file_name)
    hourly_weather = weather["hourly"]
    if hourly_weather:
        hourly_text_box.delete(1.0, END)
        for entry in hourly_weather:
            time = str(datetime.datetime.fromtimestamp(entry["dt"]))
            hourly_text_box.insert(
                END,
                f"{time[5:]}: {entry['temp']}°K, {entry['weather'][0]['description']}\n",
            )
    else:
        hourly_text_box.delete(1.0, END)
        hourly_text_box.insert(END, "File not found or invalid JSON data.")


def display_icon(icon_id):
    url = f"https://openweathermap.org/img/w/{icon_id}.png"
    try:
        response = requests.get(url)
        icon_data = response.content
        icon = Image.open(BytesIO(icon_data))
        icon = icon.resize((60, 60))  # Adjust the size as needed
        icon = ImageTk.PhotoImage(icon)

        # Display the icon in a Label widget
        icon_label.config(image=icon, bg="#57ADFF")
        icon_label.image = icon  # Keep a reference to prevent garbage collection
    except Exception as e:
        error_img = ImageTk.PhotoImage(
            file="E:\Code\Python\Sketch\WeatherApp\error.png"
        )
        icon_label.config(image=error_img)


def close_app():
    closeapp = tkinter.messagebox.askyesno(
        "Do you want to exit App?", "The app is still in development tho"
    )
    if closeapp > 0:
        app.destroy()
        return


# Create the main application window
app = Tk()
app.title("Hourly Weather App")
app.geometry("890x470+300+300")
app.configure(bg="#57ADFF")
app.resizable(False, False)

# Menu bar testing

menubar = Menu(app)
app.configure(menu=menubar)
submenu1 = Menu(menubar, tearoff=False)
menubar.add_cascade(label="App", menu=submenu1)

submenu1.add_command(label="Exit", command=close_app)
submenu1.add_command(label="Refresh")

# Create widgets
file_label = Label(app, text="Display:")
# file_entry = Entry(app)
icon_label = Label(app, image=PhotoImage(file="04d.png"))
get_weather_button = Button(
    app, text="Display Hourly Weather", command=display_hourly_weather
)
hourly_text_box = Text(app, width=45, height=10)
daily_text_box = Text(app, width=45, height=10)
result_label = Label(app, fg="red")

box_img = ImageTk.PhotoImage(file="E:\Code\Python\Sketch\WeatherApp\Images\\box.png")

weather_sector1 = Label(image=box_img,border=0)
# Place widgets on the window------------------
# file_label.pack()
# file_entry.pack()
# get_weather_button.pack()
display_hourly_weather()
display_daily_weather()
daily_text_box.place(x=379, y=100)
hourly_text_box.place(x=0, y=180)

display_icon("10d")
icon_label.pack()
weather_sector1.place(x=45,y=250)
# result_text.grid(column=5)


# Start the Tkinter main loop------------------
app.mainloop()
