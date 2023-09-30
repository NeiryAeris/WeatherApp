from tkinter import *
import tkinter.messagebox
import datetime
import json


# def read_hourly_weather_data(file_path):
#     try:
#         with open(file_path, "r") as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         return None

file_name = "testing_data.json"

def read_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def display_hourly_weather():
    # file_path = file_entry.get()
    # weather = read_hourly_weather_data(file_path)
    weather = read_data(file_name)
    hourly_weather = weather["hourly"]
    if hourly_weather:
        result_text.delete(1.0, END)
        for entry in hourly_weather:
            result_text.insert(
                END,
                f"{datetime.datetime.fromtimestamp(entry['dt'])}: {entry['temp']}°K, {entry['weather'][0]['description']}\n",
            )
    else:
        result_text.delete(1.0, END)
        result_text.insert(END, "File not found or invalid JSON data.")


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
file_label = Label(app, text="Display:")
# file_entry = Entry(app)
get_weather_button = Button(
    app, text="Display Hourly Weather", command=display_hourly_weather
)
result_text = Text(app, width=40, height=10)

# Place widgets on the window
file_label.pack()
# file_entry.pack()
get_weather_button.pack()
result_text.pack()
# result_text.grid(column=5)

# Start the Tkinter main loop
app.mainloop()
