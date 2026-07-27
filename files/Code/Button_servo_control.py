# This part is just to tell the program it is working on a raspberry pico pi
from machine import Pin, PWM
import time

# The following tells the program names of the components attached to the raspberry pico pi 
# Connect GP16 to the "signal" pin of the servo motor
servo_pin = Pin(16)
#Tell the program that PWM is needed to control the servo
servo = PWM(servo_pin)
# Connect one end of the button to GP14 and the other end to VSYS
#button = Pin(14, Pin.IN)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

#Define the max and min duty cycles
max_duty = 7800 # This means 100% duty cycle to the raspberry pico pi
min_duty = 1800 # This means 0% duty cycle to the raspberry pico pi

# Set the PWM frequency
frequency = 50
servo.freq(frequency)

while True:
    # if the button is pressed, turn the motor to max angle
    if button.value() == 1:
        servo.duty_u16(max_duty)
        time.sleep(1)
    # if the button is not pressed, turn the motor to min angle
    else:
        servo.duty_u16(min_duty)
        time.sleep(1)
    time.sleep(0.1)

