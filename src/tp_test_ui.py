import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import queue
import sys
import os


# os.path.expanduser("~\Desktop") + "\\"

# current_time = time.strftime('%Y%m%d%H%M%S', time.gmtime(int(each_device.shell("date +%s"))))
# with open(file_save_path + "/screenshot_" + current_time + ".png", "wb") as fp:
#     fp.write(result)

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)
#
# telematics_test_apk_path = resource_path('venv/Lib/external_apk/TelematicsTest.apk')


class UI():
    def __init__(self):
        self.q = queue.Queue()
        self.source_dbc = []
        self.number_of_signals_ready = 0
        self.tx_signals_from_ui = {}
        self.ready_signals = []

ui = UI()


def print_tp_data():
    original_text = entry_tp_data.get()
    print("original_text: ", original_text)
    encoded_text = original_text.encode("utf-16be")
    print("encoded_text: ", encoded_text)
    print(type(encoded_text))
    data = []
    for each in encoded_text:
        data.append(hex(each))
        print(hex(each))

    print(data)


###
root_window = tk.Tk()
root_window.wm_title("VEK TP Test Tool")
# root_window.geometry("640x400+100+100")
# # geometry("Width x Height + Initial location x coordinate + Initial location y coordinate")
root_window.resizable(False, False)
# resizable(Height, Width)

p1_f1 = tk.LabelFrame(root_window, text='DBC Setting', bg='#6495ed', bd=5, padx=5, pady=5, width=100)
p1_f1.grid(row=0, column=0, sticky='nsew')

entry_tp_data = tk.Entry(p1_f1, width=20)
entry_tp_data.grid(row=0, column=0, sticky='nsew')

btn_dbc_channel_1 = tk.Button(p1_f1, text="Print TP Data", width=15, command=lambda: print_tp_data())
btn_dbc_channel_1.grid(row=0, column=1, sticky='nsew')
################

root_window.pack_propagate(0)
