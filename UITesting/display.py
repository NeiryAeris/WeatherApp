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
                f"{time[5:]}: {str(int(entry['temp']['day'] - 273.15))[:4]}°C, {entry['weather'][0]['description']}\n",
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
                f"{time[5:]}: {str(int(entry['temp'] - 273.15))[:4]}°C, {entry['weather'][0]['description']}\n",
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
daily_label = Label(app, text="Daily:")
hourly_label = Label(app, text="Hourly:")
# file_entry = Entry(app)
icon_label = Label(app, image=PhotoImage(file="04d.png"))
get_weather_button = Button(
    app, text="Display Hourly Weather", command=display_hourly_weather
)

hourly_text_box = Text(app, width=40, height=5)
daily_text_box = Text(app, width=40, height=5)
result_label = Label(app, fg="red")

box_img = ImageTk.PhotoImage(file="Images\\box.png")
base_img = ImageTk.PhotoImage(file="Images\\base.png")
weather_sector = Label(image=box_img, border=0)
base_sector = Label(image=box_img, border=0)


frame = Frame(app, width=900, height=155, bg="#212120")

big_img = ImageTk.PhotoImage(file="Images\\main.png")
main_sector = Label(frame, image=big_img, border=0)
sub_img = ImageTk.PhotoImage(file="Images\\sub.png")
sub1_sector = Label(frame, image=sub_img, border=1)
sub2_sector = Label(frame, image=sub_img, border=1)
sub3_sector = Label(frame, image=sub_img, border=1)
sub4_sector = Label(frame, image=sub_img, border=1)
sub5_sector = Label(frame, image=sub_img, border=1)
sub6_sector = Label(frame, image=sub_img, border=1)


weat_data = read_data(file_name)

temperature = int(weat_data["current"]["temp"]) - 273.15
temp = Label(
    app,
    text=f"Temperature: {str(temperature)[:4]}°C",
    bg="#203243",
    fg="white",
    font=("Helvetica",10)
)
temp.place(x=42, y=125)

feels_like = int(weat_data["current"]["feels_like"]) - 273.15
feels = Label(
    app,
    text=f"Feels like: {str(feels_like)[:4]}°C",
    bg="#203243",
    fg="white",
    font=("Helvetica",10)
)
feels.place(x=42, y=150)

humidity = weat_data["current"]["humidity"]
humid = Label(
    app, text=f"Humidity: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10)
)
humid.place(x=42, y=175)

description = weat_data["current"]["weather"][0]["description"]
descript = Label(
    app, text=f"Overall: {description}", bg="#203243", fg="white", font=("Helvetica",10)
)
descript.place(x=42, y=200)


# Place widgets on the window------------------
daily_label.place(x=398, y=80)
daily_text_box.place(x=399, y=100)

hourly_label.place(x=398, y=190)
hourly_text_box.place(x=399, y=210)
# file_entry.pack()
# get_weather_button.pack()
display_hourly_weather()
display_daily_weather()

# icon_label.pack()
weather_sector.place(x=40, y=120)

frame.place(x=0,y=320)
main_sector.place(x=10, y=10)
sub1_sector.place(x=280,y=10)
sub2_sector.place(x=420,y=10)
sub3_sector.place(x=560,y=10)
sub4_sector.place(x=700,y=10)
sub5_sector.place(x=840,y=10)
sub6_sector.place(x=980,y=10)
# result_text.grid(column=5)


# Start the Tkinter main loop------------------
app.mainloop()
