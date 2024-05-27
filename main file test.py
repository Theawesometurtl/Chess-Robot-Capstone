#main file

import RPi.GPIO as GPIO
from time import sleep

from limit_switch import switch_state
from stepper_motor import move_CW, move_CCW
from servo_motor import move_continuous_servoCW, hold_angle_continuous_servo, move_continuous_servoCCW, p
p.start(0)
move_continuous_servoCW()
sleep(1)
hold_angle_continuous_servo()
sleep(1)
move_continuous_servoCCW()
sleep(1)
p.stop()