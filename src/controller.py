import RPi.GPIO as GPIO
import time
class Controller:

    # CLOCKWISE = 0
    # ANTICLOCKWISE = 1
    DEBOUNCE = 200

    def __init__(self, clockPin, dataPin, buttonPin, rotaryCallback, buttonPressCallback):
        #persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.rotaryCallback = rotaryCallback
        self.buttonPressCallback = buttonPressCallback
        self.buttonPin = buttonPin
        #setup pins
        GPIO.setup(clockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(buttonPin, GPIO.IN)

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING,
            callback=self._clockCallback, bouncetime=self.DEBOUNCE)
        GPIO.add_event_detect(self.buttonPin, GPIO.FALLING, callback=self.buttonPressCallback,
        bouncetime=self.DEBOUNCE)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.buttonPin)

    def _clockCallback(self, pin):
        self.rotaryCallback(GPIO.input(self.dataPin))

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
