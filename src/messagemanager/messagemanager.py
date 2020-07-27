from .dbcmanager import *
from .txmanager import *


class MessageManager:
    dbc_and_tx_message_list = []

    def load_dbc(self, dbc_path_, channel_):
        dbc_manager.load_dbc(dbc_path_, channel_)

    def unload_dbc(self):
        dbc_manager.unload_dbc()

    def print_loaded_dbc_list(self):
        dbc_manager.print_loaded_dbc_list()

    def tx_message_ready_by_signal(self, tx_signals_from_ui_):
        # INPUT:    signal name, signal value
        dbc_m_tx_m_list = []
        for each_signal in tx_signals_from_ui_:
            found_dbc_and_message_tuple_list = dbc_manager.find_message_by_signal(each_signal)
            if len(found_dbc_and_message_tuple_list) > 0:
                for each_dbc_and_message in found_dbc_and_message_tuple_list:
                    found_already_exist = self.true_if_message_already_exists(each_dbc_and_message[1])
                    if found_already_exist != False:
                        print("temp_tx_message_ready_by_signal() - The message already exists")
                        found_already_exist.set_signal_value(each_signal, tx_signals_from_ui_[each_signal])
                    else:
                        dbc = each_dbc_and_message[0]
                        dbc_message = each_dbc_and_message[1]
                        signal_name_initial_min_max_list = dbc_manager.get_signals_name_initial_min_max_values(dbc.path, dbc_message.name)

                        new_tx_message = tx_message_manager.new_tx_message(dbc.path,
                                                                           dbc.channel,
                                                                           dbc_message.name,
                                                                           dbc_message.frame_id,
                                                                           dbc_message.cycle_time,
                                                                           signal_name_initial_min_max_list
                                                                           )
                        new_dbc_message_tx_message = self.new_dbc_and_tx_message(dbc, dbc_message, new_tx_message)
                        dbc_m_tx_m_list.append(new_dbc_message_tx_message)

                        new_dbc_message_tx_message.set_signal_value(each_signal, tx_signals_from_ui_[each_signal])

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
                    result = each
        else:
            result = False

        return result


message_manager = MessageManager()


class DbcMessageTxMessage:
    # Class that has dbc_message and tx_message paired.
    def __init__(self, dbc, dbc_message, tx_message):
        self.dbc = dbc
        self.dbc_message = dbc_message
        self.tx_message = tx_message

    def encode_tx_signals(self):
        print(self.tx_message.tx_message_signal_dict)
        encoded = self.dbc_message.encode(self.tx_message.tx_message_signal_dict)
        self.tx_message.update_encoded_signals(encoded)

    def set_signal_value(self, signal_name_, signal_value_):
        self.tx_message.tx_message_signal_dict[signal_name_] = signal_value_
        self.encode_tx_signals()



'''
from .dbcmanager import *
from .txmanager import *


class MessageManager:
    dbc_and_tx_message_list = []

    def load_dbc(self, dbc_path_, channel_):
        dbc_manager.load_dbc(dbc_path_, channel_)

    def print_loaded_dbc_list(self):
        dbc_manager.print_loaded_dbc_list()

    def tx_message_ready_by_signal(self, tx_signals_from_ui_):
        # INPUT:    signal name, signal value
        dbc_m_tx_m_list = []
        for each_signal in tx_signals_from_ui_:
            found_dbc_and_message_tuple_list = dbc_manager.find_message_by_signal(each_signal)
            if len(found_dbc_and_message_tuple_list) > 0:
                for each_dbc_and_message in found_dbc_and_message_tuple_list:
                    found_already_exist = self.true_if_message_already_exists(each_dbc_and_message[1])
                    if found_already_exist != False:
                        print("temp_tx_message_ready_by_signal() - The message already exists")
                        found_already_exist.set_signal_value(each_signal, tx_signals_from_ui_[each_signal])
                    else:
                        dbc = each_dbc_and_message[0]
                        dbc_message = each_dbc_and_message[1]
                        signal_name_initial_min_max_list = dbc_manager.get_signals_name_initial_min_max_values(dbc.path, dbc_message.name)

                        new_tx_message = tx_message_manager.new_tx_message(dbc.path,
                                                                           dbc.channel,
                                                                           dbc_message.name,
                                                                           dbc_message.frame_id,
                                                                           dbc_message.cycle_time,
                                                                           signal_name_initial_min_max_list
                                                                           )
                        new_dbc_message_tx_message = self.new_dbc_and_tx_message(dbc, dbc_message, new_tx_message)
                        dbc_m_tx_m_list.append(new_dbc_message_tx_message)

                        new_dbc_message_tx_message.set_signal_value(each_signal, tx_signals_from_ui_[each_signal])

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
                    result = each
        else:
            result = False

        return result


message_manager = MessageManager()


class DbcMessageTxMessage:
    # Class that has dbc_message and tx_message paired.
    def __init__(self, dbc, dbc_message, tx_message):
        self.dbc = dbc
        self.dbc_message = dbc_message
        self.tx_message = tx_message

    def encode_tx_signals(self):
        print(self.tx_message.tx_message_signal_dict)
        encoded = self.dbc_message.encode(self.tx_message.tx_message_signal_dict)
        self.tx_message.update_encoded_signals(encoded)

    def set_signal_value(self, signal_name_, signal_value_):
        self.tx_message.tx_message_signal_dict[signal_name_] = signal_value_
        self.encode_tx_signals()

'''