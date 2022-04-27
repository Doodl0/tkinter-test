import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

x = 0

def handle_click(event):
    print("The button was clicked!")

def handle_click2(event):
    global x
    print(x)
    x = x+1
    
label = tk.Label(text=x)

button = ttk.Button(text="Click me!")
button2 = tk.Button(text="Add 1")

label.pack()
button.pack()
button2.pack()

button.bind("<Button-1>", handle_click)

button2.bind("<Button-1>", handle_click2)

window.mainloop()


