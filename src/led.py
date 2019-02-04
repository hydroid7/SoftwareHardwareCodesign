import RPi.GPIO as GPIO

LED = [25, 8, 7, 1]

GPIO.setmode(GPIO.BCM)



# Set up pins
for pin in LED:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def reset():
    for pin in LED:
        GPIO.output(pin, GPIO.LOW)

def setLed(index, high):
    # print("INdex is: " + str(index))
    # if len(LED) >= index:
    #     raise ValueError('Out of bounds: ' + str(index))
    GPIO.output(LED[index], GPIO.HIGH if high else GPIO.LOW)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
