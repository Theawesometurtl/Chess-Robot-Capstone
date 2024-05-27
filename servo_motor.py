import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
                        
GPIO.setup(17,GPIO.OUT)
p = GPIO.PWM(17, 50)
p.start(0)

def move_servo():
    p.ChangeDutyCycle(12.5)
    sleep(.5)
    '''
    p.ChangeDutyCycle(5)
    sleep(.5)
    p.ChangeDutyCycle(7.5)
    sleep(.5)
    p.ChangeDutyCycle(10)
    sleep(.5)
    p.ChangeDutyCycle(12.5)
    sleep(.5)
    p.ChangeDutyCycle(10)
    sleep(.5)
    p.ChangeDutyCycle(7.5)
    sleep(.5)
    '''
    p.stop()
    GPIO.cleanup()
move_servo()