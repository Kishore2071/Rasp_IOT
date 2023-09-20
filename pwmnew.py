import RPi.GPIO as GPIO

channel = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 0.5)
p.start(100)
i = None
try:
    while i != 'q':
        try:
            d = input('Set a duty cycle: ')
            f = input('Set a frequency: ')

            if(d=='q' or f=='q'):
                break
            
            p.ChangeDutyCycle(int(d))
            p.ChangeFrequency(int(f))

        except ValueError as e:
            pass

except KeyboardInterrupt as e:
    print('Received Ctrl+c ->Quitting...')
    pass

p.stop()
GPIO.cleanup()
print('I am exiting')