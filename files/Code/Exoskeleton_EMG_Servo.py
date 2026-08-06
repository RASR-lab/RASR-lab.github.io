# This part is just to tell the program it is working on a raspberry pico pi
from machine import Pin, PWM, ADC
import time

# The following tells the program names of the components attached to the raspberry pico pi 
# Connect GP16 to the "signal" pin of the servo motor
servo_pin = Pin(16)
# Connect GP28 to the "ENV" pin of the Electromyograph sensor
emg = ADC(2)
led = Pin("LED", Pin.OUT)

#Tell the program that PWM is needed to control the servo
servo = PWM(servo_pin)

#Define the max and min duty cycles
max_duty = 6500 # This means 100% duty cycle to the raspberry pico pi
min_duty = 3000 # This means 0% duty cycle to the raspberry pico pi

# Set the PWM frequency
frequency = 50
servo.freq(frequency)

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
        servo.duty_u16(max_duty) # Set servo motor angle to max
        #led.value(1) 
        time.sleep(0.2)
    else:
        servo.duty_u16(min_duty) # Set servo motor angle to min
        #led.value(0) 
        time.sleep(0.2)
    
    # Now we shift the value provided by the sensor by 1 sample
    emg_1 = emg_0
    emg_2 = emg_1
    emg_3 = emg_2
    emg_4 = emg_3
    
    time.sleep(0.1)
    


