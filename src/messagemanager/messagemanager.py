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
    found_message_list = dbc_manager.find_message_by_signal_from_db(signal_name_)

    for each_message in found_message_list:
        print("Found Message: ", each_message.name)
        dbc_manager.get_signals_and_default_values(each_message)

    print("END")

