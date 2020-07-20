import tkinter as tk
from tkinter import ttk
import threading
import queue


class UI():
    def __init__(self):
        self.q = queue.Queue()



def testcommand():
    ui.q.put("test")
    print("testcommand")


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

btn_test = tk.Button(p1_f1, text="TEST", command=testcommand)
btn_test.grid(row=0, column=0)


###
root_window.pack_propagate(0)


