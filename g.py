#Python is High End language built oer c


import RPi.GPIO as GPIO    #Importing Raspberry Pi GPIO pins controller module
import time                #Importing timer module


GPIO.setmode(GPIO.BOARD)   # Set Gpio pins tag in a board setting.
GPIO.setwarnings(False)    # Turn off all warnings of sf.


#Assigning the sensor a respective pin number
#Open Terminal in Rasperry Pi; Type Pinout to inform yourself on the different pins.
moisture = 7               #the moisture pin is given 7
rain = 10                  #the rain sensor is given 10

#Assigning the Power Relay Module respective pin number
relay_1 = 5                
relay_2 = 3                


GPIO.setup(moisture, GPIO.IN)      #
GPIO.setup(rain, GPIO.IN)          #
GPIO.setup(relay_1, GPIO.OUT)      #
GPIO.setup(relay_2, GPIO.OUT)      #
Raining = False                    # Set initial data as false

GPIO.output(relay_1, False)        #
GPIO.output(relay_2, False)        #



def irrigating_pump_actuator(moisture):                           #
    if GPIO.input(moisture) == 1:                                 #
        print('Soil is Dry!')
        if GPIO.input(rain) == 0:
            print("it is raining tho!, so i won't pump water")
        elif GPIO.input(rain) == 1:
            print('Soil is dry but not raining')
            GPIO.output(relay_1, True)
    elif GPIO.input(moisture) == 0:
        print('---------------------------')
        print('Enough Water is in the soil')
        print('---------------------------')
        GPIO.output(relay_1, False)
        


GPIO.add_event_detect(moisture, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(moisture, callback=irrigating_pump_actuator)
