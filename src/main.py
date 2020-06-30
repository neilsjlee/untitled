from messagemanager import *


dbc_from_ui = {
    "C:/Workstation/DB_CFG/SU2/v08_One_C-CAN_SU2r_b_20052020.dbc": 0,
    "C:/Workstation/DB_CFG/SU2/20200522_SU2r_2021_Multi_CLU_v0.3.dbc": 1,
    "C:/Users/nehru/Desktop/20160426_2.44.03_m171207_CCAN_ON_LX2_DN8_SK3.dbc": 0,
    "C:/Users/nehru/Desktop/20181030_DN8_MCAN_2019_18-10-04.dbc": 1
}


# load_dbc(db1_path, 0)

for each_key in dbc_from_ui:
    load_dbc(each_key, dbc_from_ui[each_key])

dbc_manager.print_loaded_dbc_list()

# print(find_message_name_by_signal_from_db("ABS_W_LAMP"))
tx_message_ready_by_signal("ABS_W_LAMP", 1)