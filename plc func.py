import sys

sys.path.append("../robo_cafe_juice_v2")
import snap7
import snap7.types
import snap7.util
from Drivers.data_block_declarations  import * 

client = snap7.client.Client()  # PLC Client connection defined
client.connect("192.168.0.41", 0, 1)  # Establish connection with PLC with IP - BLOCK&SLOT defined
state = client.get_connected()  # the connection state of PLC True if connected

plc_state = client.get_cpu_state()
# print (state)

data_blocks = []  # Define a list array for all data blocks of PLC

for _ in range(294):  # The range of the list is 51 the number of data blocks in PLC
    data_block_dic = {  # define dictionary for the list
        "DB Number": 0,  # The Data block number in the plc
        "length": 0,  # The max size of address in the data block
        "data": bytearray()  # the data of data block in hex
    }
    data_blocks.append(data_block_dic)

# _______Datablock machines data

data_blocks[1]["length"] = all_data_len  # datablock: all data
# data_blocks[61]["data"] = client.db_read(61, 0, 3)
data_blocks[1]["DB Number"] = all_data_db


# _______Datablock machines data

data_blocks[7]["length"] = refilling_sensors_db_len  # datablock: refilling data
data_blocks[7]["DB Number"] = refilling_sensors_db

def add_db_size(db_num, size):  # function to add & define data block from PLC
    data_blocks[db_num]["DB Number"] = db_num  # define the data block number and save the data in the same list num
    data_blocks[db_num]["length"] = size  # define the data block addresses length
    data_blocks[db_num]['data'] = client.db_read(db_num, 0, size)  # define and save the data block data


def send_int(db, add, input_b):  # function to send int to PLC
    #   print("PLC State of Connection:", local_state)
    data = bytearray(2)  # bytearray of int the
    snap7.util.set_int(data, 0, input_b)
    client.db_write(db, add, data)  # The data is sent in hex format meaning:decimal 20 the PLC output 14
    global data_blocks  # call the global variable
    max_size = data_blocks[db]["length"]
    data_blocks[db]["data"] = client.db_read(db, 0, max_size)  # Update the data block inside the code
    sent = snap7.util.get_int(data_blocks[db]["data"], add)


def read_int(db, add):  # function to read int to PLC

    #   print("PLC State of Connection:", local_state)
    data = bytearray(2)  # bytearray of int the
    global data_blocks  # call the global variable
    max_size = data_blocks[db]["length"]
    data_blocks[db]["data"] = client.db_read(db, 0, max_size)  # Update the data block inside the code
    reading = snap7.util.get_int(data_blocks[db]["data"], add)
    return reading


def read_bool(db, add, input_b):
    global data_blocks  # call the global variable
    max_size = data_blocks[db]["length"]
    data_blocks[db]["data"] = client.db_read(db, 0, max_size)
    reading_bool = snap7.util.get_bool(data_blocks[db]["data"], add, input_b)
    return reading_bool


def send_bool(db, add, input_b, sta):  # Function to send true or false to PLC
    reading = client.db_read(db, add, 1)  # Read 1 byte from db staring from address
    snap7.util.set_bool(reading, 0, input_b, sta)  # Set a state of input bit
    client.db_write(db, add, reading)  # Write back the boolean value to be changed in the PLC.
    global data_blocks  # call the global variable
    max_size = data_blocks[db]["length"]
    data_blocks[db]["data"] = client.db_read(db, 0, max_size)
    # print(snap7.util.get_bool(data_blocks[db]["data"], add, input_b))


def send_string(db, add, str_text):  # function to send String to PLC //string_text the text input to be sent
    data = bytearray(20)  # bytearray of string with 254 len
    snap7.util.set_string(data, 0, str_text, 255)
    client.db_write(db, add, data)  # Write string on address add in data block DB
    global data_blocks  # call the global variable
    max_size = data_blocks[db]["length"]
    data_blocks[db]["data"] = client.db_read(db, 0, max_size)
    print(data_blocks[db]["data"])
    print(snap7.util.get_string(data, 0, max_size))
    print("PLC State of Connection:", client.get_connected())


def read_string(db, len):  # function to send String to PLC //string_text the text input to be sent
    #this function not working proberly 
    data = bytearray(20)  # bytearray of string with 254 len
    global data_blocks  # call the global variable
    max_size = data_blocks[db]["length"]
    data_blocks[db]["data"] = client.db_read(db, 6,len)
    hex = data_blocks[db]["data"].decode()
    string = snap7.util.get_string(data,4)

    # string =  snap7.util.get_fstring(data, 4, 15)
    # string = snap7.util.get_string(data,add)
    # print(string)
    # print("PLC State of Connection:", client.get_connected())
    return string 

def send_dint(db, add, dint):
    data = bytearray(4)
    snap7.util.set_dint(data, 0, dint)
    client.db_write(db, add, data)  # Write string on address add in data block DB
    global data_blocks  # call the global variable
    max_size = data_blocks[db]["length"]
    data_blocks[db]["data"] = client.db_read(db, 0, max_size)
    print("PLC State of Connection:", client.get_connected())

def read_array_bytes(db, start  , len):
    data = client.db_read(db, start, len)
    return data.decode('utf-8')

