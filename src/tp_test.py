import time
import can


bus1 = can.Bus(interface='vector', channel=0)
bus2 = can.Bus(interface='vector', channel=1)


##################
# AV BT TP
'''
tp_task1 = bus2.send_periodic(can.Message(arbitration_id=0x122, extended_id=False, data=[0x08, 0x40, 0x00, 0x00, 0x00, 0x00, 0x02, 0x13]), 0.2)
time.sleep(3)
tp_task1.modify_data(can.Message(arbitration_id=0x122, extended_id=False, data=[0x08, 0x44, 0x00, 0x00, 0x00, 0x00, 0x02, 0x13]))
time.sleep(0.5)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x10, 0x20, 0xF8, 0xAD, 0x00, 0xB3, 0x7c, 0xB9]))
tp_task1.modify_data(can.Message(arbitration_id=0x122, extended_id=False, data=[0x08, 0x40, 0x00, 0x00, 0x00, 0x00, 0x02, 0x13]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x21, 0x20, 0x00, 0xAC, 0xC0, 0x91, 0xB7, 0x58]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x22, 0xD5, 0x94, 0xB2, 0x20, 0x00, 0x31, 0x00]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x23, 0x30, 0x00, 0x00, 0xAC, 0xC0, 0xC9, 0x20]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x24, 0x00, 0x74, 0xC7, 0x20, 0xC7, 0xAA, 0xAA]))
'''
# HINDI "गाने का नाम"
tp_task1 = bus2.send_periodic(can.Message(arbitration_id=0x122, extended_id=False, data=[0x08, 0x40, 0x00, 0x00, 0x00, 0x00, 0x02, 0x13]), 0.2)
time.sleep(3)
tp_task1.modify_data(can.Message(arbitration_id=0x122, extended_id=False, data=[0x08, 0x44, 0x00, 0x00, 0x00, 0x00, 0x02, 0x13]))
time.sleep(0.5)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x10, 0x20, 0x17, 0x09, 0x3e, 0x09, 0x28, 0x09]))
tp_task1.modify_data(can.Message(arbitration_id=0x122, extended_id=False, data=[0x08, 0x40, 0x00, 0x00, 0x00, 0x00, 0x02, 0x13]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x21, 0x47, 0x09, 0x20, 0x00, 0x15, 0x09, 0x3e]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x22, 0x09, 0x20, 0x00, 0x28, 0x09, 0x3e, 0x09]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x23, 0x2e, 0x09, 0x31, 0x00, 0x32, 0x00, 0x33]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x24, 0x00, 0x34, 0x00, 0x35, 0x00, 0xAA, 0xAA]))


time.sleep(3)
bus2.send(can.Message(arbitration_id=0x4F6, extended_id=False, data=[0x02, 0x00, 0x00, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA]))
### Clear TP
time.sleep(5)

'''
##################
# TBT Destination TP
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x03, 0xF4, 0x00, 0x00, 0xAA, 0xAA, 0xAA, 0xAA]))
time.sleep(0.1)

bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x10, 0x20, 0xF4, 0x00, 0xF8, 0xAD, 0x00, 0xB3]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x21, 0x7c, 0xB9, 0x20, 0x00, 0xAC, 0xC0, 0x91]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x22, 0xB7, 0x58, 0xD5, 0x94, 0xB2, 0x20, 0x00]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x23, 0x31, 0x00, 0x30, 0x00, 0x00, 0xAC, 0xC0]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x24, 0xC9, 0x20, 0x00, 0x74, 0xC7, 0x20, 0xC7]))


time.sleep(3)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x02, 0x00, 0x00, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA]))
### Clear TP
time.sleep(5)
'''

##################
# TBT Destination TP
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x03, 0xF4, 0x00, 0x00, 0xAA, 0xAA, 0xAA, 0xAA]))
time.sleep(0.1)

bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x10, 0x08, 0xF4, 0x00, 0x88, 0xD7, 0x88, 0xD7]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x21, 0x88, 0xD7, 0x20, 0x00, 0xAC, 0xC0, 0x91]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x22, 0xB7, 0x58, 0xD5, 0x94, 0xB2, 0x20, 0x00]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x23, 0x31, 0x00, 0x30, 0x00, 0x00, 0xAC, 0xC0]))
time.sleep(0.02)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x24, 0xC9, 0x20, 0x00, 0x74, 0xC7, 0x20, 0xC7]))


time.sleep(3)
bus2.send(can.Message(arbitration_id=0x49B, extended_id=False, data=[0x02, 0x00, 0x00, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA]))
### Clear TP