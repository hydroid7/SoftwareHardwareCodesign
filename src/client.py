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

READINGS = ROOT.get_children()[0].get_children()[1].get_children()
# print(var)
while True:
    with open('test.csv', 'a') as writeFile:
        current_line = []
        for value in READINGS:
            current_line.append(value.get_value())
        WRITER = csv.writer(writeFile)
        WRITER.writerow(current_line)
    time.sleep(4)
