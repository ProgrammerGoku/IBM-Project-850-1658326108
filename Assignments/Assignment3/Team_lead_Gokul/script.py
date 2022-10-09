##################     BLINKING LED PROGRAM    ########################

import RPi.GPIO as GPIO 

from time import sleep

GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

while True: 
 GPIO.output(8, GPIO.HIGH) 
 sleep(1)
 GPIO.output(8, GPIO.LOW) 
 sleep(1)

#################  TRAFFIC LIGHT   #######################
from gpiozero import LED

red=LED(22)
green=LED(25)
amber=LED(8)

while true:
    red.on()
    sleep(2)
    amber.on()
    sleep(2)
    green.on()
    sleep(2)
    

