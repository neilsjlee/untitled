import ctypes

ask_dll = ctypes.cdll.LoadLibrary("C:/Users/slee113/PycharmProjects/untitled\src/lib/ASK/SU2/HKMC_AdvancedSeedKey_Win32.dll")

py_arr = [1, 2, 3, 4, 5, 6, 7, 8]
c_arr = (ctypes.c_byte * len(py_arr))(*py_arr)
print(c_arr[5])


py_arr2 = [0, 0, 0, 0, 0, 0, 0, 0]
return_key_array = (ctypes.c_byte * len(py_arr2))(*py_arr2)

ask_dll.ASK_KeyGenerate(c_arr, return_key_array)

i=0
while (i < 8):
    if return_key_array[i] < 0:
        return_key_array[i] = return_key_array[i] * -1
    temp = int(return_key_array[i]).to_bytes(1, 'big')
    print(temp)
    # print(temp.to_bytes(1, byteorder="big"))
    i = i+1

print("done")