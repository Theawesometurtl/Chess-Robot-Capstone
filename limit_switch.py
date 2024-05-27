import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SWITCH_PIN = 16

DEBOUNCE_TIME_MS = 1

GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

switch_state = GPIO.input(SWITCH_PIN)

def button_callback(channel):
    global switch_state
    switch_state = GPIO.input(SWITCH_PIN)
    print(switch_state)
    
GPIO.add_event_detect(SWITCH_PIN, GPIO.BOTH, callback=button_callback, bouncetime=DEBOUNCE_TIME_MS)
  

