# This part is just to tell the program it is working on a raspberry pico pi
from machine import Pin
import time

# The following tells the program names of the components attached to the raspberry pico pi 
# Onboard LED is usually on GP25 or "LED"
led = Pin("LED", Pin.OUT)

while True:
    led.value(1)       # Change LED state (ON -> OFF or OFF -> ON)
    time.sleep(2)    # Delay in seconds
    led.value(0)
    time.sleep(0.5)    # Delay in seconds
