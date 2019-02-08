import time
import RPi.GPIO as GPIO
class Controller(object):
    """
    Interacts with the controller interface. Watches GPIOs for the turning button
    and press.
    """
    DEBOUNCE = 200

    def __init__(self, clock_pin, data_pin, button_pin, rotary_callback, button_press_callback):
        #persist values
        self.__clock_pin__ = clock_pin
        self.__data_pin__ = data_pin
        self.__rotary_callback__ = rotary_callback
        self.__button_press_callback__ = button_press_callback
        self.__button_pin__ = button_pin
        #setup pins
        GPIO.setup(clock_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(data_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button_pin, GPIO.IN)

    def start(self):
        """
        Set up the usage of GPIO pins. Finally it has to be closed.
        """
        GPIO.add_event_detect(self.__clock_pin__, GPIO.FALLING,
                              callback=self._clock_callback,
                              bouncetime=self.DEBOUNCE)
        GPIO.add_event_detect(self.__button_pin__, GPIO.FALLING,
                              callback=self.__button_press_callback__,
                              bouncetime=self.DEBOUNCE)
        return self

    def stop(self):
        GPIO.remove_event_detect(self.__clock_pin__)
        GPIO.remove_event_detect(self.__button_pin__)
        GPIO.cleanup()
        return self

    def _clock_callback(self, pin):
        self.__rotary_callback__(GPIO.input(self.__data_pin__))

#test
if __name__ == "__main__":

    print('Program start.')

    CLOCKPIN = 14
    DATAPIN = 15

    def rotaryChange(datapin):
        print( "turned - " + str(datapin))

    def buttonpress(channel):
        print("press button")

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
