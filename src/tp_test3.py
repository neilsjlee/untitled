from tp_test_ui import *

test = u'그대를'
print(test)
encoded = test.encode("utf-16be")

print(encoded)

for each in encoded:
    print(each)


tp_input = '17	9	30	9	40	9	2C	9	20	0	1A	9	41	9	28	9	4D	9	28	9	42	9	20	0	15	9	40	9	20	0	36	9	48	9	24	9	3E	9	28	9	3F	9	2F	9	3E	9	2	9	20	0	4D	0	6F	0	72	0	61	0	6C	0	20	0	53	0	74	0	6F	0	72	0	69	0	65	0	73	0	20	0	7C	0	20	0	42	0	65	0	64	0	74	0	69	0	6D	0	65	0	20	0	53	0	74	0	6F	0	72	0	69	0	65	0	73	0	20	0	7C	0	20	0'
parsed_data = tp_input.split('\t')
switched_data = []

counter = 0

for each in parsed_data:
    print(each)

    if counter%2 == 0:
        switched_data.append('temp')
        switched_data.append('temp')
        switched_data[counter+1] = each
    if counter%2 == 1:
        switched_data[counter-1] = each
    counter = counter + 1
print("counter: ", counter)
print(switched_data)


result_string = ""
counter2 = 0

for each in switched_data:
    if counter2%2 == 0:
        result_string = result_string + "&#x"
        if len(each) == 1:
            result_string = result_string + "0" + each
        else:
            result_string = result_string + each
    if counter2 % 2 == 1:
        if len(each) == 1:
            result_string = result_string + "0" + each
        else:
            result_string = result_string + each
        result_string = result_string + ";"
    counter2 = counter2 + 1

print(result_string)

root_window.mainloop()