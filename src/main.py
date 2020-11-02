from messagemanager import *
from ui import *
import threading

'''
dbc_from_ui = {
    "C:/Workstation/DB_CFG/SU2/v08_One_C-CAN_SU2r_b_20052020.dbc": 0,
    "C:/Workstation/DB_CFG/SU2/20200522_SU2r_2021_Multi_CLU_v0.3.dbc": 1,
    "C:/Users/nehru/Desktop/20160426_2.44.03_m171207_CCAN_ON_LX2_DN8_SK3.dbc": 0,
    "C:/Users/nehru/Desktop/20181030_DN8_MCAN_2019_18-10-04.dbc": 1
}

tx_signals_from_ui = {
    "ABS_W_LAMP": 1,
    "TCS_LAMP": 1,
    "CF_Gway_AutoLightValue": 1
}


for each_key in dbc_from_ui:
    message_manager.load_dbc(each_key, dbc_from_ui[each_key])

message_manager.print_loaded_dbc_list()

ready_messages = []
ready_messages = message_manager.tx_message_ready_by_signal(tx_signals_from_ui)

for each in ready_messages:
    print(each.tx_message.tx_message_name, each.tx_message.tx_message_id, each.tx_message.tx_signals)
    print("\t", each.tx_message.tx_message_signal_dict)
'''


class MainThread(threading.Thread):
    ready_messages = []

    def run(self):
        print("main_thread_running")
        while True:
            try:
                data = ui.q.get()
            except:
                count = 0
            if data == "test":
                print("MainThread: TEST")
            if data == "load_dbc":
                print("MainThread: LOAD DBC")
                message_manager.unload_dbc()
                for each_item in ui.source_dbc:
                    for each_key in each_item.keys():
                        message_manager.load_dbc(each_key, each_item[each_key])
                message_manager.print_loaded_dbc_list()
            if data[0] == "add_signals":
                self.ready_messages = message_manager.tx_message_ready_by_signal(ui.tx_signals_from_ui)
                for each in self.ready_messages:
                    print(each.tx_message.tx_message_name, each.tx_message.tx_message_id, each.tx_message.tx_signals)
                    print("\t", each.tx_message.tx_message_signal_dict)

                ui.tx_signals_from_ui.clear()

    # def pass_ready_signals_from_mmgr_to_ui(self):



main_thread = MainThread()
MainThread().start()

root_window.mainloop()

