import tkinter as tk
from PIL import Image, ImageTk

# Create a Tkinter window
window = tk.Tk()
window.title("Transparent Image Overlay Example")

# Load the background image
background_image = Image.open("Images\\rain_weather.png")
background_photo = ImageTk.PhotoImage(file="Images\\rain_weather.png")

# Create a Canvas widget and place it in the window
canvas = tk.Canvas(window, width=background_image.width, height=background_image.height)
canvas.pack()

# Display the background image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Load the transparent overlay image
overlay_image = Image.open("images\Rounded Rectangle 3.png")
overlay_photo = ImageTk.PhotoImage(file="images\Rounded Rectangle 3.png")

# Display the transparent overlay image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=overlay_photo)
canvas.config(highlightthickness=0)
# Run the Tkinter main loop
window.mainloop()