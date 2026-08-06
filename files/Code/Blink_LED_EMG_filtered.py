# This part is just to tell the program it is working on a raspberry pico pi
from machine import Pin, ADC
import time

# The following tells the program names of the components attached to the raspberry pico pi 
# Connect GP28 to the "ENV" pin of the Electromyograph sensor
emg = ADC(2)
led = Pin("LED", Pin.OUT)

# This part is to filter the EMG sensor data
emg_0 = 0 # This variable holds the current sensor value
emg_1 = 0 # This variable holds the sensor value right before the current value
emg_2 = 0 # This variable holds the sensor value 2 samples before the current value
emg_3 = 0 # This variable holds the sensor value 3 samples before the current value
emg_4 = 0 # This variable holds the sensor value 4 samples before the current value
threshold = 2000 # This is the value the sensor needs to reach for anything to happen

while True:
    # The following is a simple filter
    emg_0 = emg.read_u16()
    emg_avg = (emg_0 + emg_1 + emg_2 + emg_3 + emg_4)/5
    
    # This line just prints the value of 
    print(emg_avg)
    
    if emg_avg > threshold:
        led.value(1) 
        time.sleep(0.2)
    else:
        led.value(0) 
        time.sleep(0.2)
    
    # Now we shift the value provided by the sensor by 1 sample
    emg_1 = emg_0
    emg_2 = emg_1
    emg_3 = emg_2
    emg_4 = emg_3
    
    time.sleep(0.1)
    


