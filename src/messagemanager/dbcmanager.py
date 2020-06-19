import cantools
import re


class DbcManager:
    dbc_list = []
    # def __init__(self):


class Dbc:
    def __init__(self, path, channel, loaded_dbc):
        self.path = path
        self.channel = channel
        self.loaded_dbc = loaded_dbc


dbc_manager = DbcManager()


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
    '''
    for each_dbc in dbc_manager.dbc_list:
        db_file = open(each_dbc.path, "r")
        print(db_file)
        message_line = ''
        for line in db_file:
            if line.startswith("BO_ "):
                message_line = line
                message_line_parse_ID = hex(int(message_line.split(" ")[1]))
                message_line_parse_name = (message_line.split(" ")[2]).split(":")[0]
            if line.startswith(" SG_"):
                # CASE INSENSITIVE search using RE
                if re.search(signal_name, line, re.IGNORECASE):
                    found_message_ID = message_line_parse_ID
                    found_message_name = message_line_parse_name
                    print('Message Info: ', found_message_ID, found_message_name)
                    print('Signal Info: ', line)
                    found_messages_list.append(found_message_name)

        db_file.close
    '''

    for each_dbc in dbc_manager.dbc_list:
        for each_message in each_dbc.loaded_dbc.messages:
            for each_signal in each_message.signals:
                if re.search(each_signal.name, signal_name_, re.IGNORECASE):
                    found_message_ID = each_message.frame_id
                    found_message_name = each_message.name
                    found_messages_list.append(found_message_name)

    return found_messages_list


def get_message_attributes():
    # DBC
    # Channel
    # Message ID
    # Message Name
    # Message Cycle Time
    # Signals Name
    # Signals Initial value
    #
    print("get_message_attributes")