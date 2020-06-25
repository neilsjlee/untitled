import cantools
import re


class DbcManager:
    dbc_list = []
    # def __init__(self):

    def load_dbc(self, dbc_path, channel):
        try:
            self.dbc_list.append(Dbc(dbc_path, channel, cantools.database.load_file(dbc_path)))
        except:
            print("Load DBC Error: Please check DBC path")

    def print_loaded_dbc_list(self):
        for each_dbc in self.dbc_list:
            print("Loaded DBC Path:", each_dbc.path, "\tX\tChannel:", each_dbc.channel)

    def find_message_by_signal_from_db(self, signal_name_):
        # Search input signal name from the DBCs loaded.
        found_messages_list = []

        for each_dbc in self.dbc_list:
            for each_message in each_dbc.loaded_dbc.messages:
                for each_signal in each_message.signals:
                    if re.search(each_signal.name, signal_name_, re.IGNORECASE):
                        found_messages_list.append(each_message)

        return found_messages_list

    def get_message_attributes(self, message_name_):
        # DBC
        # Channel
        # Message ID
        # Message Name
        # Message Cycle Time
        # Signals Name
        # Signals Initial value
        #
        print("get_message_attributes")

    def get_signals_and_default_values(self, message_):
        signal_list = []
        for each_signal in message_.signals:
            signal_info_tuple = (each_signal.name, each_signal.initial, each_signal.minimum, each_signal.maximum)
            print("\t", each_signal.name, ", ", each_signal.initial, ", ", each_signal.minimum, ", ", each_signal.maximum)
            signal_list.append(signal_info_tuple)

        return signal_list


class Dbc:
    def __init__(self, path, channel, loaded_dbc):
        self.path = path
        self.channel = channel
        self.loaded_dbc = loaded_dbc


dbc_manager = DbcManager()


'''
def load_dbc(dbc_path, channel):
    try:
        dbc_manager.dbc_list.append(Dbc(dbc_path, channel, cantools.database.load_file(dbc_path)))
    except:
        print("Load DBC Error: Please check DBC path")


def print_loaded_dbc_list():
    for each_dbc in dbc_manager.dbc_list:
        print("Loaded DBC Path:", each_dbc.path, "\tX\tChannel:", each_dbc.channel)


def find_message_name_by_signal_from_db(signal_name_):
    # Search input signal name from the DBCs loaded.
    found_messages_list = []

    for each_dbc in dbc_manager.dbc_list:
        for each_message in each_dbc.loaded_dbc.messages:
            for each_signal in each_message.signals:
                if re.search(each_signal.name, signal_name_, re.IGNORECASE):
                    found_message_ID = each_message.frame_id
                    found_message_name = each_message.name
                    found_messages_list.append(found_message_name)

    return found_messages_list


def get_message_attributes(message_name_):
    # DBC
    # Channel
    # Message ID
    # Message Name
    # Message Cycle Time
    # Signals Name
    # Signals Initial value
    #

    print("get_message_attributes")
'''