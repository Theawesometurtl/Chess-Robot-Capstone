import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)


class Servo:
    def __init__(self, pin1):
        self.pin1 = pin1
        GPIO.setup(pin1, GPIO.OUT)
        self.p = GPIO.PWM(pin1, 50)
        self.p.start(0)

    def angle_to_duty(self, angle):
        return float(angle) / 18 + 2

    def hold_angle_continuous_servo(self):
        duty = self.angle_to_duty(97)
        print(duty)
        self.p.ChangeDutyCycle(duty)

    def move_continuous_servoCW(self):
        duty = self.angle_to_duty(75)
        print(duty)
        self.p.ChangeDutyCycle(duty)

    def move_continuous_servoCCW(self):
        duty = self.angle_to_duty(150)
        print(duty)
        self.p.ChangeDutyCycle(duty)

    def move_180_servo(self, end_angle):
        duty = self.angle_to_duty(end_angle)
        print(duty, end_angle)
        sleep(0.1)
        self.p.ChangeDutyCycle(duty)

    def move_180_servo_slow(self, start_angle, end_angle):
        for angle in range(start_angle, end_angle):
            duty = self.angle_to_duty(angle)
            print(duty, angle)
            sleep(0.1)
            self.p.ChangeDutyCycle(duty)

def lower_claw():
    pass

    
servo1 = Servo(17)                        
