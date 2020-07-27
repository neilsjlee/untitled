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

    def unload_dbc(self):
        if len(self.dbc_list) > 0:
            del self.dbc_list[:]

    def print_loaded_dbc_list(self):
        for each_dbc in self.dbc_list:
            print("Loaded DBC Path:", each_dbc.path, "\tX\tChannel:", each_dbc.channel)

    def find_message_by_signal(self, signal_name_):
        # INPUT:    signal name
        # OUTPUT:   message list (found_messages_list)

        found_messages_list = []

        for each_dbc in self.dbc_list:
            for each_message in each_dbc.loaded_dbc.messages:
                for each_signal in each_message.signals:
                    if re.fullmatch(signal_name_, each_signal.name, re.IGNORECASE):
                        dbc_message_tuple = (each_dbc, each_message)
                        found_messages_list.append(dbc_message_tuple)

        return found_messages_list

    def get_signals_name_initial_min_max_values(self, db_path_, message_name_):
        # INPUT:    dbc path, message name
        # OUTPUT:   List[tuple(signal name, signal init value, signal minimum value, signal maximum value)]

        loaded_dbc = self.find_loaded_dbc(db_path_)
        signal_list = []
        for each_signal in (loaded_dbc.get_message_by_name(message_name_)).signals:
            signal_info_tuple = (each_signal.name, each_signal.initial, each_signal.minimum, each_signal.maximum)
            signal_list.append(signal_info_tuple)

        return signal_list

    def get_message_attributes(self, db_path_, message_name_):
        # Message ID
        # Message Name
        # Message Cycle Time
        loaded_dbc = self.find_loaded_dbc(db_path_)

        message_id = loaded_dbc.get_message_by_name(message_name_).frame_id
        cycle_time = loaded_dbc.get_message_by_name(message_name_).cycle_time

        return message_id, cycle_time

    def find_loaded_dbc(self, db_path_):
        # INPUT:    db path
        # OUTPUT:   loaded dbc
        for each_dbc in self.dbc_list:
            if each_dbc.path == db_path_:
                found_loaded_dbc = each_dbc.loaded_dbc
        return found_loaded_dbc


class Dbc:
    def __init__(self, path, channel, loaded_dbc):
        self.path = path
        self.channel = channel
        self.loaded_dbc = loaded_dbc


dbc_manager = DbcManager()

