import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title('Progress Bar')

bar = ttk.Progressbar(master=window, orient='horizontal', length=500, mode='determinate')

bar.pack()

btn_start = ttk.Button(master=window, text="Start", command=bar.start)

btn_start.pack(side = tk.LEFT)

btn_stop = ttk.Button(master=window, text="Stop", command=bar.stop)

btn_stop.pack(side = tk.LEFT)

btn_step = ttk.Button(master=window, text="Step", command=bar.step)

btn_step.pack(side = tk.LEFT)

window.mainloop()
