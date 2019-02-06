import datetime
import RPi.GPIO as GPIO
import time
from led import Counter, Direction
from controller import Controller
c = Counter()

# def rotaryChange(datapin):
#     print("rotaryChange")
#     c.count(Direction.UP)
#
# def buttonpress(channel):
#     if channel == 18: # Button
#         c.count(Direction.UP)
#
#
# GPIO.setmode(GPIO.BCM)
# ky040 = Controller(14, 15, 18, rotaryChange, buttonpress)
print('Program start.')

CLOCKPIN = 14
DATAPIN = 15

def rotaryChange(datapin):
    print( "turned - " + str(datapin))
    if datapin > 0:
        c.count(Direction.UP)
    else:
        c.count(Direction.DOWN)

def buttonpress(channel):
    print("press button")
    c.count(Direction.UP)

GPIO.setmode(GPIO.BCM)
ky040 = Controller(CLOCKPIN, DATAPIN, 18, rotaryChange, buttonpress)

print( 'Launch switch monitor class.')

ky040.start()
print( 'Start program loop...')
try:
    while True:
        time.sleep(10)
finally:
    print( 'Stopping GPIO monitoring...')
    ky040.stop()
    GPIO.cleanup()
    print( 'Program ended.')
