import time
from pprint import pprint

bus_channel_1 = 0
bus_channel_2 = 0


class TxMessageManager:
    tx_message_list = []

    def check_if_the_same_message_already_ready(self, dbc_path_, message_name_):
        for each_tx_message in self.tx_message_list:
            if (each_tx_message.tx_db_path == dbc_path_) & (each_tx_message.tx_message_name == message_name_):
                print("The same message is already ready in TxMessageManager")


class TxMessage:
    # db_path, channel, message_name, message_id, message_cycle_time
    # signal_dict, encoded_signals, send_task
    tx_message_signal_dict = {}
    encoded_signals = ""
    send_task = ""

    def __init__(self, tx_db_path, tx_channel, tx_message_name, tx_message_id, tx_message_cycle):
        self.tx_db_path = tx_db_path
        self.tx_channel = tx_channel
        self.tx_message_name = tx_message_name
        self.tx_message_id = tx_message_id
        self.tx_message_cycle = tx_message_cycle

    def start_send_periodically(self):
        if self.tx_channel == 0:
            # send_task = bus_channel_1.send_periodic(temp_message, 0.2, store_task=False)
            print("TBD")


tx_message_manager = TxMessageManager()


def set_bus(channel_, bus_):
    if (channel_ == 0):
        bus_channel_1 = bus_
    elif (channel_ == 1):
        bus_channel_2 = bus_
    else:
        print("Unknown channel")

