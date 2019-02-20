import time
import csv
from opcua import Client

CLIENT = Client("opc.tcp://10.20.50.102:4840/")

CLIENT.connect()
ROOT = CLIENT.get_root_node()
OBJECTS = CLIENT.get_objects_node()

# Node objects have methods to read and write node attributes as
# well as browse or populate address space
print("Children of root are: ", ROOT.get_children())

# Returns true if arr1[0..n-1] and  
# arr2[0..m-1] contain same elements. 
def are_equal(arr_1, arr_2): 
    # Linearly compare elements 
    for i in range(0, len(arr_1)): 
        if (arr1[i] != arr2[i]): 
            return False; 
    # If all elements were same. 
    return True;

READINGS = ROOT.get_children()[0].get_children()[1].get_children()
last_line = []
while True:
    with open('/home/pi/hardware-software-codesign/test.csv', 'a') as writeFile:
        current_line = []
        for value in READINGS:
            current_line.append(value.get_value())
        if not are_equal(last_line, current_line):
            WRITER = csv.writer(writeFile)
            WRITER.writerow(current_line)
            print("Row written...")
    time.sleep(3)

def set_value(node, new_val):
    """
    Sets the value of the node with the index `node`.
    """
    READINGS[node].set_value(new_val)
