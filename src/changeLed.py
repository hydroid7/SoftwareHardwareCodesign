import sys
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

def set_value(node, new_val):
    """
    Sets the value of the node with the index `node`.
    """
    READINGS[node].set_value(new_val)
print(str(sys.argv))
set_value(int(sys.argv[1]), bool(sys.argv[2]))
