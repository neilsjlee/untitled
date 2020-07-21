import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import queue


class UI():
    def __init__(self):
        self.q = queue.Queue()
        self.source_dbc = {}


def open_dbc(channel):
    if channel == 0:
        file = filedialog.askopenfilenames(initialdir="C:/Workstation/DB_CFG/", title="Choose DBC for Channel 1", filetypes=(("DBC files", "*.dbc"),("All files","*.*")))
        for each in file:
            ui.source_dbc[each] = 0
            print(ui.source_dbc)
    if channel == 1:
        file = filedialog.askopenfilenames(initialdir="C:/Workstation/DB_CFG/", title="Choose DBC for Channel 2", filetypes=(("DBC files", "*.dbc"),("All files","*.*")))
        for each in file:
            ui.source_dbc[each] = 1
            print(ui.source_dbc)


def load_dbc():
    if len(ui.source_dbc) > 0:
        ui.q.put("load_dbc")
    else:
        messagebox.showerror("No DBC File Added", "Please add DBC files first")


ui = UI()

###
root_window = tk.Tk()
root_window.wm_title("VEK Simple CAN Tool")
root_window.geometry("640x400+100+100")
# geometry("Width x Height + Initial location x coordinate + Initial location y coordinate")
root_window.resizable(False, False)
# resizable(Height, Width)

notebook = ttk.Notebook(root_window)
notebook_p1 = tk.Frame(notebook)
notebook.add(notebook_p1, text='Page 1')
notebook.grid(row=1, rowspan=4, column=0, columnspan=4, sticky='nsew')

p1_f1 = tk.Frame(notebook_p1)
p1_f1.grid(row=0, column=0, sticky='nsew')

btn_test = tk.Button(p1_f1, text="TEST", command=lambda: ui.q.put("test"))
btn_test.grid(row=0, column=0)

btn_dbc_channel_1 = tk.Button(p1_f1, text="Add CAN Channel 1 DB", command=lambda: open_dbc(0))
btn_dbc_channel_1.grid(row=1, column=0)

btn_dbc_channel_2 = tk.Button(p1_f1, text="Add CAN Channel 2 DB", command=lambda: open_dbc(1))
btn_dbc_channel_2.grid(row=2, column=0)

btn_load_dbc = tk.Button(p1_f1, text="Load DBCs", command=lambda: load_dbc())
btn_load_dbc.grid(row=1, column=4)
###
root_window.pack_propagate(0)
