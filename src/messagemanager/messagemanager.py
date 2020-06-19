from .dbcmanager import *
from .hwsetup import *
from .txmanager import *


def tx_message_ready(signal_name_, signal_value_):
    find_message_name_by_signal_from_db(signal_name_)
    print("END")