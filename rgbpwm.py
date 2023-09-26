import RPi.GPIO as GPIO
from time import sleep

channel=[12,13,19]

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

try:
    while True:
        print("Enter input as 1's and 0's:\n")
        r=int(input("Red: "))
        g=int(input("Green: "))
        b=int(input("Blue: "))

        if r==1:
            GPIO.output(12, GPIO.HIGH)
        if r==0:
            GPIO.output(12, GPIO.LOW)     
        if g==1:
            GPIO.output(13, GPIO.HIGH)
        if g==0:
            GPIO.output(13, GPIO.LOW)
        if b==1:
            GPIO.output(19, GPIO.HIGH)
        if b==0:
            GPIO.output(19, GPIO.LOW)
        

except KeyboardInterrupt as e:
    print('\nReceived Ctrl+c ->Quitting...')
    pass

print('I am exiting')