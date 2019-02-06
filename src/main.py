# import led
# import counter

# from counter import Direction
# from counter import Counter
# from random import randint
import datetime
import RPi.GPIO as GPIO
import time
from led import Counter, Direction

c = Counter()
cont = Controller()
def buttonpress(channel):
    # led.reset()
    if channel == 18: # Button
        c.count(Direction.UP)
        # c.increment(Direction.UP)
        # for idx, item in enumerate(c.toBin()):
        #     if item:
        #         led.setLed(idx, item)


def turn(channel):
    pass
    # if GPIO.input(23)==0:
    #     GPIO.output(23, GPIO.HIGH)
    # elif GPIO.input(23)==1:
    #     GPIO.output(23, GPIO.LOW)

GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonpress,
bouncetime=200)

#GPIO.add_event_detect(14, GPIO., callback=turn)

try:
    while True:
        time.sleep(5)
        #GPIO.output(23, 1)

# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:
        GPIO.cleanup()

# print(counter(30, Direction.UP))
# print(counter(30, Direction.DOWN))
# print(counter(0, Direction.DOWN))
#
#
# print(toBin(10))
# print(toBin(20))
