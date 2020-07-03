from .dbcmanager import *
from .hwsetup import *
from .txmanager import *

set_bus(0, bus1)
set_bus(1, bus2)


class MessageManager:
    dbc_and_tx_message_list = []

    def load_dbc(self, dbc_path_, channel_):
        dbc_manager.load_dbc(dbc_path_, channel_)

    def print_loaded_dbc_list(self):
        dbc_manager.print_loaded_dbc_list()

    def temp_tx_message_ready_by_signal(self, signal_name_, signal_value_):
        # INPUT:    signal name, signal value
        dbc_m_tx_m_list = []

        found_dbc_and_message_tuple_list = dbc_manager.find_message_by_signal(signal_name_)
        if len(found_dbc_and_message_tuple_list) > 0:
            for each_dbc_and_message in found_dbc_and_message_tuple_list:
                if self.true_if_message_already_exists(each_dbc_and_message[1]):
                    print("temp_tx_message_ready_by_signal() - The message already exists")
                else:
                    dbc = each_dbc_and_message[0]
                    dbc_message = each_dbc_and_message[1]
                    new_tx_message = tx_message_manager.new_tx_message(dbc.path,
                                                                       dbc.channel,
                                                                       dbc_message.name,
                                                                       dbc_message.frame_id,
                                                                       dbc_message.cycle_time
                                                                       )
                    dbc_m_tx_m_list.append(self.new_dbc_and_tx_message(dbc, dbc_message, new_tx_message))

        return dbc_m_tx_m_list

    def new_dbc_and_tx_message(self, dbc_, dbc_message_, new_tx_message_):
        new = DbcMessageTxMessage(dbc_, dbc_message_, new_tx_message_)
        self.dbc_and_tx_message_list.append(new)
        return new

    def true_if_message_already_exists(self, dbc_message_):
        result = False

        if len(self.dbc_and_tx_message_list) > 0:
            for each in self.dbc_and_tx_message_list:
                if each.dbc_message == dbc_message_:
                    result = True
        else:
            result = False

        return result


def tx_message_ready_by_signal(signal_name_, signal_value_):
    # INPUT:    signal name, signal value
    # OUTPUT:   db_path, channel, message_name, message_id, message_cycle_time,
    found_dbc_message_tuple_list = dbc_manager.find_message_by_signal_from_db(signal_name_)

    for each_dbc_message_tuple in found_dbc_message_tuple_list:
        db_path = each_dbc_message_tuple[0]
        channel = each_dbc_message_tuple[1]
        message_name = each_dbc_message_tuple[2]

        message_attributes_tuple = dbc_manager.get_message_attributes(db_path, message_name)
        message_id = hex(message_attributes_tuple[0])
        message_cycle_time = message_attributes_tuple[1]

        signal_name_initial_min_max_list = dbc_manager.get_signals_and_default_values(db_path, message_name)
        # signal_name_initial_min_max: [0] signal_name, [1] initialValue, [2] min, [3] max

        new_tx_message = tx_message_manager.new_tx_message(db_path,
                                                           channel,
                                                           message_name,
                                                           message_id,
                                                           message_cycle_time,
                                                           signal_name_initial_min_max_list
                                                           )

        # signal_name_value[signal_name_] = int(signal_value_, 16)
        new_tx_message.tx_message_signal_dict[signal_name_] = signal_value_



message_manager = MessageManager()


class DbcMessageTxMessage:
    # Class that has dbc_message and tx_message paired.
    def __init__(self, dbc, dbc_message, tx_message):
        self.dbc = dbc
        self.dbc_message = dbc_message
        self.tx_message = tx_message


