from threading import Thread
import RPi.GPIO as GPIO
import time
from led import Counter, Direction, LedBlock
from controller import Controller
from server import LedServer


COUNTER = Counter(LedBlock([25, 8, 7, 1]))
SERVER = LedServer("opc.tcp://10.20.50.102:4840/", "Team2")
print('Program start.')

CLOCKPIN = 14
DATAPIN = 15
BUTTONPIN = 18

def rotary_change(datapin):
    """
    Callback if the rotary button was rotated.
    """
    if datapin > 0:
        COUNTER.count(Direction.UP)
    else:
        COUNTER.count(Direction.DOWN)
    onChange()

def button_press(channel):
    """
    Callback for button press events.
    """
    if channel == BUTTONPIN:
        COUNTER.count(Direction.UP)
    onChange()

def onChange():
    SERVER.notify_clients(COUNTER.to_state())

def server_launcher():
    print("Starting server")
    SERVER.start_server()

GPIO.setmode(GPIO.BCM)
CONTROLLER = Controller(CLOCKPIN, DATAPIN, BUTTONPIN, rotary_change, button_press)
CONTROLLER.start()

THREAD = Thread(target=server_launcher)
THREAD.start()
THREAD.join()
print("Thread finished...exiting")

print("Start program loop...")
try:
    while True:
        time.sleep(10)
finally:
    CONTROLLER.stop()
    GPIO.cleanup()
    print( 'Program ended.')
