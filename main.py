#main file

import RPi.GPIO as GPIO
from time import sleep

from limit_switch import switch_state
from stepper_motor import move_CW, move_CCW
from servo_motor import move_continuous_servoCW, hold_angle_continuous_servo, move_continuous_servoCCW, p, move_180_servo, move_180_servo_slow
p.start(0)
#move_continuous_servoCW()
move_180_servo(5)
sleep(1)
move_180_servo(180)
#hold_angle_continuous_servo()
sleep(1)
#move_continuous_servoCCW()
sleep(1)
p.stop()
GPIO.cleanup()