from messagemanager import *


dbc_from_ui = {
    "C:/Workstation/DB_CFG/SU2/v08_One_C-CAN_SU2r_b_20052020.dbc": 0,
    "C:/Workstation/DB_CFG/SU2/20200522_SU2r_2021_Multi_CLU_v0.3.dbc": 1
}


# load_dbc(db1_path, 0)

for each_key in dbc_from_ui:
    load_dbc(each_key, dbc_from_ui[each_key])

print_loaded_dbc_list()

print(find_message_name_by_signal_from_db("CF_AVN_BCANValueSet"))