import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import queue


class UI():
    def __init__(self):
        self.q = queue.Queue()
        self.source_dbc = []
        self.number_of_signals_ready = 0


def open_dbc(channel):
    if channel == 0:
        file = filedialog.askopenfilenames(initialdir="C:/Workstation/DB_CFG/", title="Choose DBC for Channel 1", filetypes=(("DBC files", "*.dbc"),("All files","*.*")))
        for each in file:
            temp = {each, 0}
            ui.source_dbc.append(temp)
            list_dbc_channel_1.insert(list_dbc_channel_1.size(), each)

    if channel == 1:
        file = filedialog.askopenfilenames(initialdir="C:/Workstation/DB_CFG/", title="Choose DBC for Channel 2", filetypes=(("DBC files", "*.dbc"),("All files","*.*")))
        for each in file:
            temp = {each, 1}
            ui.source_dbc.append(temp)
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
                delete_targets1.append(list_dbc_channel_1.get(each))
            for each in delete_targets1:
                if ui.source_dbc[each] == 0:
                    del ui.source_dbc[each]
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


def add_signal():
    temp_label = tk.Label(p1_f3, text='new')
    temp_label.grid(row=ui.number_of_signals_ready, column=0)
    ui.number_of_signals_ready = ui.number_of_signals_ready + 1


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

# Page 1 - Frame 1 (p1_f1)
p1_f1 = tk.LabelFrame(notebook_p1, text='DBC Setting', bg='#6495ed', bd=5, padx=5, pady=5, width=100)
p1_f1.grid(row=0, column=0, sticky='nsew')

btn_dbc_channel_1 = tk.Button(p1_f1, text="Open CCAN DBCs", width=15, command=lambda: open_dbc(0))
btn_dbc_channel_1.grid(row=0, column=0, sticky='nsew')

list_dbc_channel_1 = tk.Listbox(p1_f1, selectmode='extended', height=3, width=75)
list_dbc_channel_1.grid(row=0, column=1, sticky='nsew')

btn_delete_dbc_channel_1 = tk.Button(p1_f1, text="Delete", width=10, command=lambda: delete_dbc(0))
btn_delete_dbc_channel_1.grid(row=0, column=2, sticky='nsew')

btn_dbc_channel_2 = tk.Button(p1_f1, text="Open MMCAN DBCs", command=lambda: open_dbc(1))
btn_dbc_channel_2.grid(row=1, column=0, sticky='nsew')

list_dbc_channel_2 = tk.Listbox(p1_f1, selectmode='extended', height=3)
list_dbc_channel_2.grid(row=1, column=1, sticky='nsew')

btn_delete_dbc_channel_2 = tk.Button(p1_f1, text="Delete", command=lambda: delete_dbc(1))
btn_delete_dbc_channel_2.grid(row=1, column=2, sticky='nsew')

btn_load_dbc = tk.Button(p1_f1, text="Load DBCs", command=lambda: load_dbc(), height=2)
btn_load_dbc.grid(row=2, column=0, columnspan=4, sticky='nsew')
################

blank_line_p1f1_p1f2 = tk.Label(notebook_p1)
blank_line_p1f1_p1f2.grid(row=2, column=0)

# Page 1 - Frame 2 (p1_f2)
p1_f2 = tk.LabelFrame(notebook_p1, text='Signal Setting', bd=5, padx=5, pady=5, width=100)
p1_f2.grid(row=3, column=0, sticky='nsew')

lbl_signal_name = tk.Label(p1_f2, text='Signal Name:', width=15)
lbl_signal_name.grid(row=0, column=0)

entry_signal_name = tk.Entry(p1_f2, width=20)
entry_signal_name.grid(row=0, column=1)

lbl_signal_value = tk.Label(p1_f2, text='Signal Value:', width=15)
lbl_signal_value.grid(row=0, column=2)

entry_signal_value = tk.Entry(p1_f2, width=20)
entry_signal_value.grid(row=0, column=3)

blank_label_p1f2 = tk.Label(p1_f2, width=20)
blank_label_p1f2.grid(row=0, column=4)

btn_add_signal = tk.Button(p1_f2, text='Add Signal', width=10, command=lambda: add_signal())
btn_add_signal.grid(row=0, column=5, sticky='nsew')

################

blank_line_p1f2_p1f3 = tk.Label(notebook_p1, width=100)
blank_line_p1f2_p1f3.grid(row=4, column=0)

# p1_f3
p1_f3 = tk.LabelFrame(notebook_p1, text='Tx Message', bd=5, padx=5, pady=5)
p1_f3.grid(row=5, column=0, sticky='nsew')


################

root_window.pack_propagate(0)
