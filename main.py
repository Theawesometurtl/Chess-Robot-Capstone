#main file

import RPi.GPIO as GPIO
from time import sleep

from limit_switch import switch_state
from stepper_motor import move_CW, move_CCW
from servo_motor import Servo, servo1, lower_claw, lift_claw
from camera.py import take_photo


#move_continuous_servoCW()
servo1.move_180_servo(5)
sleep(1)
servo1.move_180_servo(180)
#servo1.hold_angle_continuous_servo()
sleep(1)
#servo1.move_continuous_servoCCW()
sleep(1)
p.stop()
GPIO.cleanup()

def mainloop():
    take_photo()
    check_for_board_change()