# This part is just to tell the program it is working on a raspberry pico pi
from machine import Pin, PWM
import time

# The following tells the program names of the components attached to the raspberry pico pi 
# Connect GP16 to the "signal" pin of the servo motor
servo_pin = Pin(16)
#Tell the program that PWM is needed to control the servo
servo = PWM(servo_pin)

#Define the max and min duty cycles
max_duty = 7800 # This means 100% duty cycle to the raspberry pico pi
min_duty = 1800 # This means 0% duty cycle to the raspberry pico pi

# Set the PWM frequency
frequency = 150
servo.freq(frequency)

while True:
    servo.duty_u16(max_duty) # Set servo motor angle to max
    time.sleep(2)
    servo.duty_u16(min_duty) # Set servo motor angle to min
    time.sleep(2)


