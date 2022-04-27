import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

frame = tk.Frame(
    relief=tk.RIDGE,
    borderwidth= 5
)

entry = ttk.Entry(
    master = frame
)
frame.pack()
entry.pack()

entry.insert(0, "This is an entry")

window.mainloop()
