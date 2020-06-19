import time
from pprint import pprint


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


