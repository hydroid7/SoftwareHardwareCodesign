from threading import Thread
import datetime
import RPi.GPIO as GPIO
import time
from led import Counter, Direction
from controller import Controller
from server import startServer
c = Counter()

print('Program start.')

CLOCKPIN = 14
DATAPIN = 15
BUTTONPIN = 18
def rotaryChange(datapin):
    if datapin > 0:
        c.count(Direction.UP)
    else:
        c.count(Direction.DOWN)

def buttonpress(channel):
    if channel == BUTTONPIN:
        c.count(Direction.UP)

GPIO.setmode(GPIO.BCM)
controller = Controller(CLOCKPIN, DATAPIN, BUTTONPIN, rotaryChange, buttonpress)
controller.start()



def threaded_function(arg):
    print("Starting server")
    startServer()


if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    thread.start()
    thread.join()
    print ("thread finished...exiting")

print( 'Start program loop...')
try:
    while True:
        time.sleep(10)
finally:
    controller.stop()
    GPIO.cleanup()
    print( 'Program ended.')
