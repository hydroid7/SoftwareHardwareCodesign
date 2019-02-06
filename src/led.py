import RPi.GPIO as GPIO


class LedBlock:
    def __init__(self, leds):
        self.LED = leds
        GPIO.setmode(GPIO.BCM)
        for pin in self.LED:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def reset(self):
        for pin in self.LED:
            GPIO.output(pin, GPIO.LOW)

    def setLed(index, high):
        print(index)
        GPIO.output(self.LED[index], GPIO.HIGH if high else GPIO.LOW)

class Direction:
    UP = 1
    DOWN = -1

class Counter:
    __current_value__ = 0
    leds = LedBlock([25, 8, 7, 1])
    def count(self, dir):
        self.__current_value__ += dir
        if self.__current_value__ > 15:
            self.__current_value__ = 0
        elif self.__current_value__ < 0:
            self.__current_value__ = 15
        self.leds.reset()
        for id, item in enumerate(self.toBin()):
            print(item)
            if item:
                self.leds.setLed(id, item[id])
        return self

    def toBin(self):
        return map(
            lambda x: True if x == '1' else False,
            list("{:04b}".format(self.__current_value__))
        )

    def __str__(self):
        return str(self.__current_value__) + "        " + "{:04b}".format(self.__current_value__)
