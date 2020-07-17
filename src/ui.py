import tkinter as tk
from tkinter import ttk
import threading
import queue


class UI():
    def __init__(self):
        print("PLEASE UPDATE")


root_window = tk.Tk()
root_window.wm_title("VEK Simple CAN Tool")
root_window.geometry("640x400+100+100")
# geometry("Width x Height + Initial location x coordinate + Initial location y coordinate")
root_window.resizable(False, False)
# resizable(Height, Width)

device_number_label = tk.Label(root_window, text="Connected HU: ", width=25)
device_number_label.grid(row=0, column=0)

root_window.pack_propagate(0)


def main_loop():




    root_window.after(1000, main_loop)


root_window.after(1000, main_loop)




root_window.mainloop()