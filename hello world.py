import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

label = tk.Label(
    text="What is this abomination?",
    fg="white",  # Set the text color to white
    bg="#34A2FE",  # Set the background color to light blue
    width=30, # The width and height are measured in text units
    height=1
)

entry = ttk.Entry(
    width=50
)

button = tk.Button(
    text="Press to delete",
    fg="white",
    bg="purple",
    width=25, 
    height=5,  
)

image = tk.PhotoImage(file="python.png") 
 
img = tk.Label( image = image)

img.pack()

label.pack()

button.pack()

entry.pack()

entry.insert(0, "JK thats not how it works")

window.mainloop()
