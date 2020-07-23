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
            list_dbc_channel_1.insert(list_dbc_channel_1.size(), each)

    if channel == 1:
        file = filedialog.askopenfilenames(initialdir="C:/Workstation/DB_CFG/", title="Choose DBC for Channel 2", filetypes=(("DBC files", "*.dbc"),("All files","*.*")))
        for each in file:
            ui.source_dbc[each] = 1
            list_dbc_channel_2.insert(list_dbc_channel_2.size(), each)
    print(ui.source_dbc)


def delete_dbc(channel):
    if channel == 0:
        current_selected_chan1_dbc = list_dbc_channel_1.curselection()
        if current_selected_chan1_dbc == ():
            print("Empty")
        else:
            delete_targets1 = []
            for each in current_selected_chan1_dbc:
                delete_targets1.append(list_dbc_channel_2.get(each))
            for each in delete_targets1:
                if ui.source_dbc[each] == 0:
                    del ui.source_dbc[each]
                del ui.source_dbc[list_dbc_channel_1.get(each)]
            for each in current_selected_chan1_dbc[::-1]:
                list_dbc_channel_1.delete(each)

    if channel == 1:
        current_selected_chan2_dbc = list_dbc_channel_2.curselection()
        if current_selected_chan2_dbc == ():
            print("Empty")
        else:
            delete_targets2 = []
            for each in current_selected_chan2_dbc:
                delete_targets2.append(list_dbc_channel_2.get(each))
            for each in delete_targets2:
                if ui.source_dbc[each] == 1:
                    del ui.source_dbc[each]
            for each in current_selected_chan2_dbc[::-1]:
                list_dbc_channel_2.delete(each)

    print(ui.source_dbc)


def load_dbc():
    if len(ui.source_dbc) > 0:
        ui.q.put("load_dbc")
    else:
        messagebox.showerror("No DBC File Added", "Please open DBC files first")


ui = UI()

###
root_window = tk.Tk()
root_window.wm_title("VEK Simple CAN Tool")
# root_window.geometry("640x400+100+100")
# # geometry("Width x Height + Initial location x coordinate + Initial location y coordinate")
root_window.resizable(False, False)
# resizable(Height, Width)

notebook = ttk.Notebook(root_window)
notebook_p1 = tk.Frame(notebook)
notebook.add(notebook_p1, text='Page 1')
notebook.grid(row=1, rowspan=4, column=0, columnspan=4, sticky='nsew')

p1_f1 = tk.Frame(notebook_p1)
p1_f1.grid(row=0, column=0, sticky='nsew')

btn_test = tk.Button(p1_f1, text="TEST", command=lambda: ui.q.put("test"))
btn_test.grid(row=0, column=0, sticky='nsew')

btn_dbc_channel_1 = tk.Button(p1_f1, text="Open DBCs for CAN Channel 1", command=lambda: open_dbc(0))
btn_dbc_channel_1.grid(row=1, column=0, sticky='nsew')

list_dbc_channel_1 = tk.Listbox(p1_f1, selectmode='extended', height=3, width=60)
list_dbc_channel_1.grid(row=1, column=1, sticky='nsew')

btn_delete_dbc_channel_1 = tk.Button(p1_f1, text="Delete", command=lambda: delete_dbc(0))
btn_delete_dbc_channel_1.grid(row=1, column=2, sticky='nsew')

btn_dbc_channel_2 = tk.Button(p1_f1, text="Open DBCs for CAN Channel 2", command=lambda: open_dbc(1))
btn_dbc_channel_2.grid(row=2, column=0, sticky='nsew')

list_dbc_channel_2 = tk.Listbox(p1_f1, selectmode='extended', height=3, width=60)
list_dbc_channel_2.grid(row=2, column=1, sticky='nsew')

btn_delete_dbc_channel_2 = tk.Button(p1_f1, text="Delete", command=lambda: delete_dbc(1))
btn_delete_dbc_channel_2.grid(row=2, column=2, sticky='nsew')

btn_load_dbc = tk.Button(p1_f1, text="Load DBCs", command=lambda: load_dbc())
btn_load_dbc.grid(row=3, column=0, columnspan=4, sticky='nsew')
###
root_window.pack_propagate(0)
