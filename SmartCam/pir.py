import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(4):
            print("Motion Detected...")
            file = open("/var/www/html/FIFO","w")
            file.write("im")
            file.close()
            time.sleep(15) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
