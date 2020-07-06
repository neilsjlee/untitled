from .hwsetup import *
import time
from pprint import pprint


class TxMessageManager:
    tx_message_list = []

    def check_if_the_same_message_already_ready(self, dbc_path_, message_name_):
        for each_tx_message in self.tx_message_list:
            if (each_tx_message.tx_db_path == dbc_path_) & (each_tx_message.tx_message_name == message_name_):
                print("The same message is already ready in TxMessageManager")

    def new_tx_message(self, tx_db_path_, tx_channel_, tx_message_name_, tx_message_id_, tx_message_cycle_, tx_signals_):
        temp_tx_message = TxMessage(tx_db_path_, tx_channel_, tx_message_name_, tx_message_id_, tx_message_cycle_, tx_signals_)
        self.tx_message_list.append(temp_tx_message)
        return temp_tx_message

    def find_tx_message(self, tx_db_path_, tx_channel_, tx_db_message_name_):
        for each_tx_message in self.tx_message_list:
            if (each_tx_message.tx_db_path == tx_db_path_) & (each_tx_message.tx_channel == tx_channel_) &  (each_tx_message.tx_message_name == tx_db_message_name_):
                message_found = each_tx_message
        return message_found

    def start_send_all_tx_messages(self):
        for each_tx_message in self.tx_message_list:
            each_tx_message.start_sendperiodically


tx_message_manager = TxMessageManager()


class TxMessage:
    # db_path, channel, message_name, message_id, message_cycle_time
    # signal_dict, encoded_signals, send_task
    tx_message_signal_dict = {}
    encoded_signals = ""
    encoded_message = ""
    send_task = ""

    def __init__(self, tx_db_path, tx_channel, tx_message_name, tx_message_id, tx_message_cycle, tx_signals):
        self.tx_db_path = tx_db_path
        self.tx_channel = tx_channel
        self.tx_message_name = tx_message_name
        self.tx_message_id = tx_message_id
        self.tx_message_cycle = tx_message_cycle
        self.tx_signals = tx_signals
        self.tx_signals_init()

    def tx_signals_init(self):
        self.tx_message_signal_dict = {}
        for each_signal_info in self.tx_signals:
            # signal_name_value[each_signal_info[0]] = int(each_signal_info[1], 16)
            if type(each_signal_info[1]) != 'int':
                self.tx_message_signal_dict[each_signal_info[0]] = 0
            else:
                self.tx_message_signal_dict[each_signal_info[0]] = each_signal_info[1]

    def start_send_periodically(self):
        if self.tx_channel == 0:
            self.send_task = bus1.send_periodic(self.encoded_message, self.tx_message_cycle, store_task=False)
        elif self.tx_channel == 1:
            self.send_task = bus2.send_periodic(self.encoded_message, self.tx_message_cycle, store_task=False)

    def encode_message(self):
        self.encoded_message = can.Message(arbitration_id=self.tx_message_id, extended_id=False, data=self.encoded_signals)

    def update_encoded_signals(self, encoded_signals_):
        self.encoded_signals = encoded_signals_
        if self.encoded_message == "":
            self.encode_message()
        if self.send_task != "":
            self.send_task.modify_data(self.encoded_signals)



'''
def set_bus(channel_, bus_):
    global bus_channel_1
    global bus_channel_2
    if channel_ == 0:
        bus_channel_1 = bus_
    elif channel_ == 1:
        bus_channel_2 = bus_
    else:
        print("Unknown channel")

'''