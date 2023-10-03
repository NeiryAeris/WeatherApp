from tkinter import *
import tkinter.messagebox
import datetime
import json

file_name = "testing_data.json"

def fetch_today(file_name):
    weather = read_data(file_name)
    unix_exchange = str(datetime.datetime.fromtimestamp(weather['current']['dt']))
    return unix_exchange[9:11]
    
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
            daily_text_box.insert( END, f"{time[5:]}: {str(int(entry['temp']['day'])-273.15)[:4]}°C, {entry['weather'][0]['description']}\n",)

    else:
        daily_text_box.delete(1.0, END)
        daily_text_box.insert(END, "File not found or invalid JSON data.")


def display_hourly_weather():
    weather = read_data(file_name)
    hourly_weather = weather["hourly"]
    today = fetch_today(file_name)
    if hourly_weather:
        hourly_text_box.delete(1.0, END)
        for entry in hourly_weather:
            time = str(datetime.datetime.fromtimestamp(entry["dt"]))
            if time[9:11] == today:
                hourly_text_box.insert(END,f"{time[5:]}: {str(int(entry['temp'])-273.15)[:4]}°C, {entry['weather'][0]['description']}\n",)
    else:
        hourly_text_box.delete(1.0, END)
        hourly_text_box.insert(END, "File not found or invalid JSON data.")


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
app.geometry("750x440")
app.resizable(False, False)

# Menu bar testing

menubar = Menu(app)
app.configure(menu=menubar)
submenu1 = Menu(menubar, tearoff=False)
menubar.add_cascade(label="App", menu=submenu1)

submenu1.add_command(label="Exit", command=close_app)
submenu1.add_command(label="Refresh")

# temp output and label

temp_high = Label(text="Temp(high) :", width=20, font=("bold", 20), bg="#90DFD6")
temp_high_rs = Label(text="", width=20, font=("bold", 20), bg="#90DFD6")

temp_low = Label(text="Temp(low) :", width=20, font=("bold", 20), bg="#90DFD6")
temp_low_rs = Label(text="", width=20, font=("bold", 20), bg="#90DFD6")
# pressure label and fetched data
pres = Label(text="Pressure :", width=20, font=("bold", 20), bg="#90DFD6")
pres_rs = Label(text="", width=20, font=("bold", 20), bg="#90DFD6")
# humidity label and data
hum = Label(text="Humidity :", width=20, font=("bold", 20), bg="#90DFD6")
hum_rs = Label(text="", width=20, font=("bold", 20), bg="#90DFD6")

# description
desc = Label(text="Description :", width=20, font=("bold", 20), bg="#90DFD6")
des_rs = Label(text="", width=20, font=("bold", 20), bg="#90DFD6")
# country
coun = Label(text="Country :", width=20, font=("bold", 20), bg="#90DFD6")
coun_rs = Label(text="", width=20, font=("bold", 20), bg="#90DFD6")

footer_1 = Label(text="Temperature is measured in Degrees Celsius", bg="#90DFD6")
footer_2 = Label(text="Pressure in Pascals (Pa)", bg="#90DFD6")
footer_3 = Label(
    text="Humidity is measured in grams Per Kilogram of air(g/Kg)", bg="#90DFD6"
)


# Create widgets
daily_label = Label(app, text="Daily:")
hourly_label = Label(app, text="Hourly:")
# file_entry = Entry(app)
get_weather_button = Button(
    app, text="Display Hourly Weather", command=display_hourly_weather
)
hourly_text_box = Text(app, width=40, height=5)
daily_text_box = Text(app, width=40, height=5)

# Place widgets on the window------------------
# file_label.pack()
# file_entry.pack()
# get_weather_button.pack()
display_hourly_weather()
display_daily_weather()

daily_label.place(x=398,y = 80)
daily_text_box.place(x=399, y=100)

hourly_label.place(x=398,y = 190)
hourly_text_box.place(x=399, y=210)
# result_text.grid(column=5)

# Start the Tkinter main loop------------------
app.mainloop()
