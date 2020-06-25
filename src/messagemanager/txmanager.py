import time
from pprint import pprint

bus_channel_1 = 0
bus_channel_2 = 0


class TxMessageManager:
    tx_message_list = []


class TxMessage:
    def __init__(self, tx_message_name, tx_message_cycle, tx_message_signal_dict={}):
        self.tx_message_name = tx_message_name
        self.tx_message_signal_dict = tx_message_signal_dict
        self.tx_message_cycle = tx_message_cycle

    def set_message_cycle(self, cycle_time):
        self.tx_message_cycle = cycle_time


tx_message_manager = TxMessageManager()


def set_bus(channel_, bus_):
    if (channel_ == 0):
        bus_channel_1 = bus_
    elif (channel_ == 1):
        bus_channel_2 = bus_
    else:
        print("Unknown channel")

