import RPi.GPIO as GPIO

channel = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 0.5)
p.start(50)
input('Enter a key to quit: ')
p.stop()
GPIO.cleanup()