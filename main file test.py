#main file

import RPi.GPIO as GPIO
from time import sleep

from limit_switch import switch_state
from stepper_motor import move_CW, move_CCW
from servo_motor import move_servo
move_CW(1)
move_CCW(2)
move_servo()
