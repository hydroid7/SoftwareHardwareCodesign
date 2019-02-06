import RPi.GPIO as GPIO
import time
class Controller:

    # CLOCKWISE = 0
    # ANTICLOCKWISE = 1
    DEBOUNCE = 200

    def __init__(self, clockPin, dataPin, rotaryCallback):
        #persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.rotaryCallback = rotaryCallback

        #setup pins
        GPIO.setup(clockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING,
            callback=self._clockCallback, bouncetime=self.DEBOUNCE)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)

    def _clockCallback(self, pin):
        print(GPIO.input(self.dataPin))
        # print(GPIO.input(self.clockPin))
        # if GPIO.input(self.clockPin) == 0:
        #self.rotaryCallback(GPIO.input(self.dataPin), GPIO.input(self.clockPin))

        # data = GPIO.input(self.dataPin)
        # if data == 1:
        #     self.rotaryCallback(self.ANTICLOCKWISE)
        # else:
        #     self.rotaryCallback(self.CLOCKWISE)
        self.rotaryCallback(GPIO.input(self.dataPin))

#test
if __name__ == "__main__":

    print('Program start.')

    CLOCKPIN = 14
    DATAPIN = 15

    def rotaryChange(datapin):
        print( "turned - " + str(datapin))

    GPIO.setmode(GPIO.BCM)
    ky040 = Controller(CLOCKPIN, DATAPIN, rotaryChange)

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
