import time


from pprint import pprint


class TxMessageManager:
    tx_message_list = []
    print("TxMessageManager")


class TxMessage:
    def __init__(self, tx_message_name, tx_message_cycle, tx_message_signal_dict={}):
        self.tx_message_name = tx_message_name
        self.tx_message_signal_dict = tx_message_signal_dict
        self.tx_message_cycle = tx_message_cycle

    def set_message_cycle(self, cycle_time):
        self.tx_message_cycle = cycle_time






###############################################################################################
target_message = db1.get_message_by_name(find_message_name_by_signal_from_db(db1_path, src_signal_name))
print("target_message: ", target_message)


# Initialize Message Dictionary 'message_dict'
message_dict = {}
for each_signal in target_message.signals:
    message_dict[each_signal.name] = 0

message_dict[src_signal_name] = int(signal_value, 16)

temp_encoded_data = target_message.encode(message_dict)
print("temp_encoded_data: ", temp_encoded_data)


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
