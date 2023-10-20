from tkinter import *
import urllib.request
import tkinter.messagebox
import datetime
import json
from io import BytesIO
from PIL import Image, ImageTk
import requests
from subprocess import call
import OpenWeatherAPI
file_name = "data.json"

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

def get_update():
    city=textfield.get()
    OpenWeatherAPI.get_data(city)
    reload()
    
    
# Create the main application window
app = Tk()
app.title("Hourly Weather App")
app.geometry("890x470")
app.configure(bg="#57ADFF")
app.resizable(False, False)
reload=False

thunder_skies_bg = ImageTk.PhotoImage(file="Images\\thunder.png")
clear_skies_bg = ImageTk.PhotoImage(file="Images\\clear_skies.png")
rain_skies_bg = ImageTk.PhotoImage(file="Images\\rain_weather.png")

canvas = Canvas(app, width=890, height=470)
canvas.place(x=0,y=0)
canvas.create_image(0, 0, anchor=NW, image=rain_skies_bg)

canvas.config(highlightthickness=0)

##search box

search_image=PhotoImage(file="images/Rounded Rectangle 3.png")
search_box=Label(image=search_image, bg="#57adff")
search_box.place(x=230,y=30)
#textfield
textfield = Entry(search_box, justify='left', width=15, font=('poppins',25,'bold'), bg='#203243', border=0,fg='white')
textfield.place(x=90,y=10)
textfield.focus()
#weat_image
weat_image = PhotoImage(file="images/Layer 7.png")
Label(search_box, image=weat_image, bg="#203243").place(x=15,y=5)
# search_icon
search_icon = PhotoImage(file="images/Layer 6.png")
search_button=Button(search_box,image=search_icon, borderwidth=0,cursor="hand2",bg="#203243",command=get_update)
search_button.place(x=370,y=5)
#note
note=Label(app, text="click search icon to update new weather", bg="#57ADFF", fg="white", font=("Helvetica",9)).place(x=320,y=95)



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
    app, text="Display Hourly Weather"
)

hourly_text_box = Text(app, width=40, height=5)
daily_text_box = Text(app, width=40, height=5)
result_label = Label(app, fg="red")

box_img = ImageTk.PhotoImage(file="Images\\box.png")
base_img = ImageTk.PhotoImage(file="Images\\base.png")
weather_sector = Label(image=box_img, border=0)
base_sector = Label(image=box_img, border=0)


frame = Frame(app, width=890, height=155, bg="#212120")

big_img = ImageTk.PhotoImage(file="Images\\main.png")
main_sector = Label(frame, image=big_img, border=1)
sub_img = ImageTk.PhotoImage(file="Images\\sub.png")
sub1_sector = Label(frame, image=sub_img, border=1)
sub2_sector = Label(frame, image=sub_img, border=1)
sub3_sector = Label(frame, image=sub_img, border=1)
sub4_sector = Label(frame, image=sub_img, border=1)
sub5_sector = Label(frame, image=sub_img, border=1)

# Place widgets on the window------------------
# daily_label.place(x=398, y=80)
# daily_text_box.place(x=399, y=100)

# hourly_label.place(x=398, y=190)
# hourly_text_box.place(x=399, y=210)
# file_entry.pack()
# get_weather_button.pack()
display_daily_weather()

# icon_label.pack()
weather_sector.place(x=40, y=120)

frame.place(x=0,y=320)
main_sector.place(x=10, y=10)
sub1_sector.place(x=250,y=10)
sub2_sector.place(x=380,y=10)
sub3_sector.place(x=510,y=10)
sub4_sector.place(x=640,y=10)
sub5_sector.place(x=770,y=10)

def reload():
    weat_data = read_data(file_name)
    #weather_sector
    temperature = int(weat_data["current"]["temp"]) - 273.15
    temp = Label(weather_sector, text=f"Temperature: {str(temperature)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10))
    temp.place(x=10, y=10)
    feels_like = int(weat_data["current"]["feels_like"]) - 273.15
    feels = Label(weather_sector, text=f"Feels like: {str(feels_like)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10))
    feels.place(x=10, y=30)
    humidity = weat_data["current"]["humidity"]
    humid = Label(weather_sector, text=f"Humidity: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10))
    humid.place(x=10, y=50)
    description = weat_data["current"]["weather"][0]["description"]
    descript = Label(weather_sector, text=f"Overall: {description}", bg="#203243", fg="white", font=("Helvetica",10))
    descript.place(x=10, y=70)
    #end weather sector
    
    #start main_sector
    global main_icon
    main_sect_icon_id = weat_data["current"]["weather"][0]["icon"]
    main_sect_icon_url = f"http://openweathermap.org/img/w/{main_sect_icon_id}.png"
    urllib.request.urlretrieve(main_sect_icon_url, f"{main_sect_icon_id}.png")
    main_sect_img = Image.open(f"{main_sect_icon_id}.png")
    main_icon = main_sect_img.resize((50, 50))
    main_icon = ImageTk.PhotoImage(main_icon)
    main_sect_icon = Label(main_sector,image=main_icon,bg="#203243")
    main_sect_icon.place(x=0,y=40)
    
    temperature = int(weat_data["current"]["temp"]) - 273.15
    temp = Label( main_sector, text=f"Temperature: {str(temperature)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10) )
    temp.place(x=25, y=10)
    feels_like = int(weat_data["current"]["feels_like"]) - 273.15 
    feels = Label( main_sector, text=f"Feels like: {str(feels_like)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10) )
    feels.place(x=55, y=40)
    humidity = weat_data["current"]["humidity"]
    humid = Label( main_sector, text=f"Humidity: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10) )
    humid.place(x=55, y=60)
    description = weat_data["current"]["weather"][0]["description"]
    descript = Label( main_sector, text=f"Overall: {description}", bg="#203243", fg="white", font=("Helvetica",10) )
    descript.place(x=25, y=90)
    #end main_sector
    
    #start sub1_sector
    global sub1_icon
    sub1_sect_icon_id = weat_data["daily"][0]["weather"][0]["icon"]
    sub1_sect_icon_url = f"http://openweathermap.org/img/w/{sub1_sect_icon_id}.png"
    urllib.request.urlretrieve(sub1_sect_icon_url, f"{sub1_sect_icon_id}.png")
    sub1_sect_img = Image.open(f"{sub1_sect_icon_id}.png")
    sub1_icon = sub1_sect_img.resize((50, 50))
    sub1_icon = ImageTk.PhotoImage(sub1_icon)
    sub1_sect_icon = Label(sub1_sector,image=sub1_icon,bg="#203243")
    sub1_sect_icon.place(x=20,y=15)
    
    dt=str(datetime.datetime.fromtimestamp(weat_data["daily"][0]["dt"]))
    date_time=dt[8:10]+'-'+dt[5:7]
    time=Label(sub1_sector, text=date_time,  bg="#203243", fg="white", font=("Helvetica",10,'bold')).place(x=25,y=5)
    temperature = int(weat_data["daily"][0]["temp"]['day']) - 273.15
    temp = Label( sub1_sector, text=f"Temp: {str(temperature)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10) ) 
    temp.place(x=0, y=60)
    humidity = weat_data["daily"][0]["humidity"]
    humid = Label( sub1_sector, text=f"Humid: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10) )
    humid.place(x=0, y=80)
    description = weat_data["daily"][0]["weather"][0]["description"]
    descript = Label( sub1_sector, text=f"{description}", bg="#203243", fg="white", font=("Helvetica",9) )
    descript.place(x=0, y=100)
    #end sub1_sector 
    
    #start sub2_sector
    global sub2_icon
    sub2_sect_icon_id = weat_data["daily"][1]["weather"][0]["icon"]
    sub2_sect_icon_url = f"http://openweathermap.org/img/w/{sub2_sect_icon_id}.png"
    urllib.request.urlretrieve(sub2_sect_icon_url, f"{sub2_sect_icon_id}.png")
    sub2_sect_img = Image.open(f"{sub2_sect_icon_id}.png")
    sub2_icon = sub2_sect_img.resize((50, 50))
    sub2_icon = ImageTk.PhotoImage(sub2_icon)
    sub2_sect_icon = Label(sub2_sector,image=sub2_icon,bg="#203243")
    sub2_sect_icon.place(x=20,y=15)
    
    dt=str(datetime.datetime.fromtimestamp(weat_data["daily"][1]["dt"]))
    date_time=dt[8:10]+'-'+dt[5:7]
    time=Label(sub2_sector, text=date_time,  bg="#203243", fg="white", font=("Helvetica",10,'bold')).place(x=25,y=5)
    temperature = int(weat_data["daily"][1]["temp"]['day']) - 273.15
    temp = Label(sub2_sector, text=f"Temp: {str(temperature)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10) )
    temp.place(x=0, y=60)
    humidity = weat_data["daily"][1]["humidity"]
    humid = Label( sub2_sector, text=f"Humid: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10) )
    humid.place(x=0, y=80)
    description = weat_data["daily"][1]["weather"][0]["description"]
    descript = Label( sub2_sector, text=f"{description}", bg="#203243", fg="white", font=("Helvetica",9) )
    descript.place(x=0, y=100)
    #end sub2_sector
    
    #start sub3_sector
    global sub3_icon
    sub3_sect_icon_id = weat_data["daily"][2]["weather"][0]["icon"]
    sub3_sect_icon_url = f"http://openweathermap.org/img/w/{sub3_sect_icon_id}.png"
    urllib.request.urlretrieve(sub3_sect_icon_url, f"{sub3_sect_icon_id}.png")
    sub3_sect_img = Image.open(f"{sub3_sect_icon_id}.png")
    sub3_icon = sub3_sect_img.resize((50, 50))
    sub3_icon = ImageTk.PhotoImage(sub3_icon)
    sub3_sect_icon = Label(sub3_sector,image=sub3_icon,bg="#203243")
    sub3_sect_icon.place(x=20,y=15)
    
    dt=str(datetime.datetime.fromtimestamp(weat_data["daily"][2]["dt"]))
    date_time=dt[8:10]+'-'+dt[5:7]
    time=Label(sub3_sector, text=date_time,  bg="#203243", fg="white", font=("Helvetica",10,'bold')).place(x=25,y=5)
    temperature = int(weat_data["daily"][2]["temp"]['day']) - 273.15
    temp = Label( sub3_sector, text=f"Temp: {str(temperature)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10) )
    temp.place(x=0, y=60)
    humidity = weat_data["daily"][2]["humidity"]
    humid = Label( sub3_sector, text=f"Humid: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10) )
    humid.place(x=0, y=80)
    description = weat_data["daily"][2]["weather"][0]["description"]
    descript = Label( sub3_sector, text=f"{description}", bg="#203243", fg="white", font=("Helvetica",9) )
    descript.place(x=0, y=100)
    #end sub3_sector
    
    #start sub4_sector
    global sub4_icon
    sub4_sect_icon_id = weat_data["daily"][3]["weather"][0]["icon"]
    sub4_sect_icon_url = f"http://openweathermap.org/img/w/{sub4_sect_icon_id}.png"
    urllib.request.urlretrieve(sub4_sect_icon_url, f"{sub4_sect_icon_id}.png")
    sub4_sect_img = Image.open(f"{sub4_sect_icon_id}.png")
    sub4_icon = sub4_sect_img.resize((50, 50))
    sub4_icon = ImageTk.PhotoImage(sub4_icon)
    sub4_sect_icon = Label(sub4_sector,image=sub4_icon,bg="#203243")
    sub4_sect_icon.place(x=20,y=15)
    
    dt=str(datetime.datetime.fromtimestamp(weat_data["daily"][3]["dt"]))
    date_time=dt[8:10]+'-'+dt[5:7]
    time=Label(sub4_sector, text=date_time,  bg="#203243", fg="white", font=("Helvetica",10,'bold')).place(x=25,y=5)
    temperature = int(weat_data["daily"][3]["temp"]['day']) - 273.15
    temp = Label( sub4_sector, text=f"Temp: {str(temperature)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10) )
    temp.place(x=0, y=60)
    humidity = weat_data["daily"][3]["humidity"]
    humid = Label( sub4_sector, text=f"Humid: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10))
    humid.place(x=0, y=80)
    description = weat_data["daily"][3]["weather"][0]["description"]
    descript = Label( sub4_sector, text=f"{description}", bg="#203243", fg="white", font=("Helvetica",9))
    descript.place(x=0, y=100)
    #end sub4_sector
    
    #start sub5_sector
    global sub5_icon
    sub5_sect_icon_id = weat_data["daily"][3]["weather"][0]["icon"]
    sub5_sect_icon_url = f"http://openweathermap.org/img/w/{sub5_sect_icon_id}.png"
    urllib.request.urlretrieve(sub5_sect_icon_url, f"{sub5_sect_icon_id}.png")
    sub5_sect_img = Image.open(f"{sub5_sect_icon_id}.png")
    sub5_icon = sub5_sect_img.resize((50, 50))
    sub5_icon = ImageTk.PhotoImage(sub5_icon)
    sub5_sect_icon = Label(sub5_sector,image=sub5_icon,bg="#203243")
    sub5_sect_icon.place(x=20,y=15)
    
    dt=str(datetime.datetime.fromtimestamp(weat_data["daily"][4]["dt"]))
    date_time=dt[8:10]+'-'+dt[5:7]
    time=Label(sub5_sector, text=date_time,  bg="#203243", fg="white", font=("Helvetica",10,'bold')).place(x=25,y=5)
    temperature = int(weat_data["daily"][4]["temp"]['day']) - 273.15
    temp = Label( sub5_sector, text=f"Temp: {str(temperature)[:4]}°C", bg="#203243", fg="white", font=("Helvetica",10))
    temp.place(x=0, y=60)
    humidity = weat_data["daily"][4]["humidity"]
    humid = Label(sub5_sector, text=f"Humid: {humidity}%", bg="#203243", fg="white", font=("Helvetica",10))
    humid.place(x=0, y=80)
    description = weat_data["daily"][4]["weather"][0]["description"]
    descript = Label( sub5_sector, text=f"{description}", bg="#203243", fg="white", font=("Helvetica",9))
    descript.place(x=0, y=100)
    #end sub5_sector

reload()
# Start the Tkinter main loop------------------
app.mainloop()
