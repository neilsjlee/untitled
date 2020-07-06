import time
import re
import can
import cantools


##Test

src_signal_name = 'TREAD_W_LAMP'
signal_value = '0x1'

'''
target_signal_dict = {
    'CF_RCCA_WarnLh': '0x1'
}


for key in target_signal_dict.keys():
    print("Signal Name: ", key, " / Signal Value: ", target_signal_dict[key])
'''

# db1_path = 'C:/Workstation/DB_CFG/qydb/20200318_QY_2020_PT_Chassis(2nd_Gen-2ch-C)_CLU_v1.7.dbc'
db1_path = 'C:/Workstation/DB_CFG/SU2/v08_One_C-CAN_SU2r_b_20052020.dbc'
db2_path = 'C:/Workstation/DB_CFG/qydb/20200218_QY_2020_Multi_v20.02.01.dbc'


db1 = cantools.database.load_file(db1_path)
db2 = cantools.database.load_file(db2_path)
# example_message = db1.get_message_by_name('CGW1')
# pprint(example_message.signals)


bus1 = can.Bus(interface='vector', channel=0)
bus2 = can.Bus(interface='vector', channel=1)



tx_message_list = []

###############################################################################################
class tx_message:
    def __init__(self, tx_message_name, tx_message_cycle, tx_message_signal_dict={}):
        self.tx_message_name = tx_message_name
        self.tx_message_signal_dict = tx_message_signal_dict
        self.tx_message_cycle = tx_message_cycle

    def set_message_cycle(self, cycle_time):
        self.tx_message_cycle = cycle_time


###############################################################################################
def find_message_name_by_signal_from_db(dbc_file_path, signal_name):
    # Search input signal name from the DBC.
    # * If there are multiple signals with the same signal name, the last signal in the DBC will be returned.
    db_file = open(dbc_file_path, "r")
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

    db_file.close

    # return found_message_ID
    return found_message_name
###############################################################################################




###############################################################################################
target_message = db1.get_message_by_name(find_message_name_by_signal_from_db(db1_path, src_signal_name))
print("Cycle_time: ", db1.get_message_by_name(find_message_name_by_signal_from_db(db1_path, src_signal_name)).cycle_time)
print("target_message: ", target_message)


# Initialize Message Dictionary 'message_dict'
message_dict = {}
for each_signal in target_message.signals:
    message_dict[each_signal.name] = 0

message_dict[src_signal_name] = int(signal_value, 16)

temp_encoded_data = target_message.encode(message_dict)
print("temp_encoded_data: ", temp_encoded_data)

print("frame_id:", target_message.frame_id)
temp_message = can.Message(arbitration_id=target_message.frame_id, extended_id=False, data=temp_encoded_data)


###
def encode_target_message(dbc_file_path, target_signals):
    ### Input type: Dict
    ### Return type: message list
    encoded_message_list = []
    for key in target_signals.keys():
        print("Signal Name: ", key, " / Signal Value: ", target_signals[key])
        encoded_message = db1.get_message_by_name(find_message_name_by_signal_from_db(dbc_file_path, key))




    return encoded_message_list
    print("test")
###

task = bus1.send_periodic(temp_message, 0.2, store_task=False)

print("task: ", task)

time.sleep(5)



'''
# ================================================================
# Update existing Tx CAN message
# Initialize Message Dictionary 'message_dict'
message_dict2 = {}
for each_signal in target_message.signals:
    message_dict2[each_signal.name] = 1

message_dict2[src_signal_name] = int(signal_value, 16)

temp_encoded_data2 = target_message.encode(message_dict2)
print("temp_encoded_data: ", temp_encoded_data2)


temp_message2 = can.Message(arbitration_id=target_message.frame_id, extended_id=False, data=temp_encoded_data2)
'''

message_dict[src_signal_name] = 0
temp_encoded_data = target_message.encode(message_dict)
print("Changed temp_encoded_data: ", temp_encoded_data)
temp_message.data = temp_encoded_data

# Python-can > Broadcast Manager > modify_data
# https://python-can.readthedocs.io/en/master/bcm.html
task.modify_data(temp_message)
# ================================================================





time.sleep(10)


task.stop()
