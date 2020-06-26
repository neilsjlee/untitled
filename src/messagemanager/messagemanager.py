from .dbcmanager import *
from .hwsetup import *
from .txmanager import *


set_bus(0, bus1)
set_bus(1, bus2)


def load_dbc(dbc_path_, channel_):
    dbc_manager.load_dbc(dbc_path_, channel_)


def print_loaded_dbc_list():
    dbc_manager.print_loaded_dbc_list()


def tx_message_ready(signal_name_, signal_value_):
    # INPUT:    signal name, signal value
    # OUTPUT:
    found_dbc_message_tuple_list = dbc_manager.find_message_by_signal_from_db(signal_name_)

    for each_dbc_message_tuple in found_dbc_message_tuple_list:
        db_path = each_dbc_message_tuple[0]
        channel = each_dbc_message_tuple[1]
        message_name = each_dbc_message_tuple[2]

        message_attributes_tuple = dbc_manager.get_message_attributes(db_path, message_name)
        message_id = hex(message_attributes_tuple[0])
        message_cycle_time = message_attributes_tuple[1]
        print("Found Message DB: ",db_path,
              ", Channel: ", channel,
              ", Name: ", message_name,
              "ID: ", message_id,
              "Cycle Time: ", message_cycle_time
              )

        signal_name_initial_min_max_list = dbc_manager.get_signals_and_default_values(db_path, message_name)
        signal_name_value = {}
        for each_signal_info in signal_name_initial_min_max_list:
            # signal_name_value[each_signal_info[0]] = int(each_signal_info[1], 16)
            signal_name_value[each_signal_info[0]] = each_signal_info[1]
        # signal_name_value[signal_name_] = int(signal_value_, 16)
        signal_name_value[signal_name_] = signal_value_

        for each_signal in signal_name_value.keys():
            print("\t", each_signal, ":", signal_name_value[each_signal])

    print("END")

