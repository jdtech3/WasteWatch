import RPi.GPIO as GPIO

class LED:
    def __init__(self):
        self.led_pins = [7, 11, 13, 15, 29, 31]

        GPIO.setmode(GPIO.BOARD)

        for pin in self.led_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def reset(self):
        GPIO.cleanup()
    
    def on(self): 
        for pin in self.led_pins:
            GPIO.output(pin, GPIO.HIGH)

    def off(self):
        for pin in self.led_pins:
            GPIO.output(pin, GPIO.LOW)

