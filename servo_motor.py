import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
                        
GPIO.setup(17,GPIO.OUT)
p = GPIO.PWM(17, 50)
p.start(0)

def angle_to_duty(angle):
    return float(angle) / 18 + 2

def hold_angle_continuous_servo():
    duty = angle_to_duty(97)
    print(duty)
    p.ChangeDutyCycle(duty)

def move_continuous_servoCW():
    duty = angle_to_duty(75)
    print(duty)
    p.ChangeDutyCycle(duty)

def move_continuous_servoCCW():
    duty = angle_to_duty(150)
    print(duty)
    p.ChangeDutyCycle(duty)

def move_180_servo(end_angle):
    duty = angle_to_duty(end_angle)
    print(duty, end_angle)
    sleep(0.1)
    p.ChangeDutyCycle(duty)

def move_180_servo_slow(start_angle, end_angle):
    for angle in range(start_angle, end_angle):
        duty = angle_to_duty(angle)
        print(duty, angle)
        sleep(0.1)
        p.ChangeDutyCycle(duty)



    
