from messagemanager import *
import ui

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

print("END")


ui.root_window.mainloop()