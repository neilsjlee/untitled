import cantools


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

    for each_dbc in dbc_manager.dbc_list:
        print("Loaded DBC Path:", each_dbc.path, "\tX\tChannel:", each_dbc.channel)
        # print("LoadedDBC: ", each_dbc.loaded_dbc)




