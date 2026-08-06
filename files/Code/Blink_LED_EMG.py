# This part is just to tell the program it is working on a raspberry pico pi
from machine import Pin, ADC
import time

# The following tells the program names of the components attached to the raspberry pico pi 
# Connect GP28 to the "ENV" pin of the Electromyograph sensor
emg = ADC(2)
led = Pin("LED", Pin.OUT)

threshold = 2000 # This is the value the sensor needs to reach for anything to happen

while True:
    emg_0 = emg.read_u16()
    # This line just prints the value of Electromyograph sensor
    print(emg_0)
    
    if emg_0 > threshold:
        led.value(1) 
        time.sleep(0.2)
    else:
        led.value(0) 
        time.sleep(0.2)
    
    time.sleep(0.1)
    



