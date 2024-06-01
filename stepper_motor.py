from time import sleep
import RPi.GPIO as GPIO

DIR = 20 # Direction GPIO Pin
STEP = 21 # Step GPIO Pin
CW = 1 # Clockwise Roation
CCW = 0 # Counterclockwise Rotation
SPR = 200 # Steps per Revolution (360 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14, 15, 18) #Microstep Resoltion GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (1, 1, 1)}
GPIO.output(MODE, RESOLUTION['1/16'])

step_count = SPR * 16
delay = .005 / 16


class Stepper_motor:
    def __init__(self, DIR, STEP):
        self.DIR = DIR
        self.STEP = STEP
        self.MODE = (14, 15, 18)

    def move_CW(self, rotations):
        GPIO.output(DIR, CW)
        steps = rotations * step_count
        for x in range(steps):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(delay)
    def move_CCW(self, rotations):
        GPIO.output(DIR, CW)
        steps = rotations * step_count
        for x in range(steps):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(delay)
    
def move_arm(self, x: int, y: int):
    if x > 0:
        self.move_CW(x)
    elif x<0:
        self.move_CCW(-x)
    if y > 0:
        self.move_CW(y)
    elif y<0:
        self.move_CCW(-y)



def move_CW(rotations):
    GPIO.output(DIR, CW)
    steps = rotations * step_count
    for x in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

def move_CCW(rotations):
    GPIO.output(DIR, CCW)
    steps = rotations * step_count
    for x in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

stepper1 = Stepper_motor(20, 21)
