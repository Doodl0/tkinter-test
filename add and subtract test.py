import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title('Add and Subtract')

def increase():

    value = int(lbl_value["text"])

    lbl_value["text"] = value + 1

def decrease():

    value = int(lbl_value["text"])

    lbl_value["text"] = value - 1

def increase10():

    value = int(lbl_value["text"])

    lbl_value["text"] = value + 10

def decrease10():

    value = int(lbl_value["text"])

    lbl_value["text"] = value - 10

def increase100():

    value = int(lbl_value["text"])

    lbl_value["text"] = value + 100

def decrease100():

    value = int(lbl_value["text"])

    lbl_value["text"] = value - 100

frame = tk.Frame(borderwidth = 5, relief = tk.GROOVE)
frame.pack(fill=tk.BOTH, expand=True)

frame.rowconfigure(0, minsize=50, weight=1)

frame.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=50, weight=1)

btn_decrease100 = tk.Button(master=frame, text="<<<", bg="red", fg="white", command=decrease100)

btn_decrease100.grid(row=0, column=0, sticky="nsew")

btn_decrease10 = tk.Button(master=frame, text="<<", bg="red", fg="white", command=decrease10)

btn_decrease10.grid(row=0, column=1, sticky="nsew")

btn_decrease = tk.Button(master=frame, text="<", bg="red", fg="white", command=decrease)

btn_decrease.grid(row=0, column=2, sticky="nsew")


lbl_value = tk.Label(master=frame, text="0")

lbl_value.grid(row=0, column=3)


btn_increase = tk.Button(master=frame, text=">", bg="green", fg="white", command=increase)

btn_increase.grid(row=0, column=4, sticky="nsew")

btn_increase10 = tk.Button(master=frame, text=">>", bg="green", fg="white", command=increase10)

btn_increase10.grid(row=0, column=5, sticky="nsew")

btn_increase100 = tk.Button(master=frame, text=">>>", bg="green", fg="white", command=increase100)

btn_increase100.grid(row=0, column=6, sticky="nsew")


window.mainloop()
