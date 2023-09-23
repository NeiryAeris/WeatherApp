from tkinter import *
import datetime
import json


def read_hourly_weather_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None

def display_hourly_weather():
    file_path = file_entry.get()
    weather = read_hourly_weather_data(file_path)
    hourly_weather = weather['hourly']
    if hourly_weather:
        result_text.delete(1.0, END)
        for entry in hourly_weather:
            result_text.insert(END, f"{datetime.datetime.fromtimestamp(entry['dt'])}: {entry['temp']}°K, {entry['weather'][0]['description']}\n")
    else:
        result_text.delete(1.0, END)
        result_text.insert(END, "File not found or invalid JSON data.")

# Create the main application window
app = Tk()
app.title("Hourly Weather App")

# Create widgets
file_label = Label(app, text="Enter JSON File Path:")
file_entry = Entry(app)
get_weather_button = Button(app, text="Display Hourly Weather", command=display_hourly_weather)
result_text = Text(app, width=40, height=10)

# Place widgets on the window
file_label.pack(expand= True, fill= 'both')
file_entry.pack(expand= True, fill= 'both')
get_weather_button.pack(expand= True, fill= 'both')
result_text.pack(expand= True, fill= 'both')
# result_text.grid(column=5)

# Start the Tkinter main loop
app.mainloop()
