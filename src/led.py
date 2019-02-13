import collections
import RPi.GPIO as GPIO

class LedBlock(object):
    """
    Defines the hardware interface to the LED block. The constructor takes
    an array of GPIO pin numbers.
    """
    def __init__(self, leds):
        self.led = leds
        GPIO.setmode(GPIO.BCM)
        for pin in self.led:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def reset(self):
        """
        Reset the state of the pins to disabled.
        """
        for pin in self.led:
            GPIO.output(pin, GPIO.LOW)

    def set_led(self, index, high):
        """
        Set the led with the selected `index` to the value of `high`.
        """
        GPIO.output(self.led[index], GPIO.HIGH if high else GPIO.LOW)

    def set_state(self, state_tuple):
        self.set_led(0, state_tuple[0])
        self.set_led(1, state_tuple[1])
        self.set_led(2, state_tuple[2])
        self.set_led(3, state_tuple[3])

class Direction(object):
    UP = 1
    DOWN = -1

CurrentState = collections.namedtuple('CurrentState', ['led1', 'led2', 'led3', 'led4'])

class Counter(object):
    """
    Stateful counter. Initial value is `0`.
    """
    __current_value__ = 0
    __high__ = 15
    __low__ = 0

    def __init__(self, leds):
        self.leds = leds

    def count(self, direction):
        """
        Modifies the counter in the given `direction`.
        """
        self.__current_value__ += direction
        if self.__current_value__ > self.__high__:
            self.__current_value__ = self.__low__
        elif self.__current_value__ < self.__low__:
            self.__current_value__ = self.__high__
        self.leds.reset()
        for index, item in enumerate(self.to_bin()):
            self.leds.set_led(index, item)
        return self

    def set_value(self, new_val):
        """
        Sets the value of the counter to the given `new_val`.
        """
        if new_val > self.__low__ and new_val < self.__high__:
            self.__current_value__ = new_val

    def set_value_from_state(self, state):
        """
        Sets the value of the counter based on the state object.
        """
        self.set_value(state[0] + 2 * state[1] + 4 * state[2] + 8 * state[3])

    def to_int_array(self):
        return list(map(
            lambda x: int(x),
            list("{:04b}".format(self.__current_value__))
        ))

    def to_bin(self):
        """
        Converts the counter to its binary representation.
        """
        return map(
            lambda x: True if x == '1' else False,
            list("{:04b}".format(self.__current_value__))
        )

    def to_state(self):
        values = self.to_int_array()
        return CurrentState(values[0], values[1], values[2], values[3])

    def __str__(self):
        return str(self.__current_value__) + "        " + "{:04b}".format(self.__current_value__)
