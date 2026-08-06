# This part is just to tell the program it is working on a raspberry pico pi
from machine import Pin
import time

# The following tells the program names of the components attached to the raspberry pico pi 
# Onboard LED is usually on GP25 or "LED"
led = Pin("LED", Pin.OUT)
# Connect one end of the button to GP14 and the other end to VSYS
#button = Pin(14, Pin.IN)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.value(1)       # Change LED state (ON -> OFF or OFF -> ON)
        time.sleep(0.1)
    else:
        led.value(0)
        time.sleep(0.1)
    time.sleep(0.1)
