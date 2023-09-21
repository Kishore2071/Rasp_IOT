import RPi.GPIO as GPIO

channel = [17,27,22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

dc=100
freq=None
i = None

p = GPIO.PWM(channel, 0.5)
p.start(dc)

try:
    while i != 'q':
        try:
            dc = input('Set a duty cycle: ')
            freq = input('Set a frequency: ')

            if(dc=='q' or freq=='q'):
                break
            
            p.ChangeDutyCycle(int(dc))    # where dc is the duty cycle (0.0 <= dc <= 100.0)
            p.ChangeFrequency(int(freq))  # where freq is the new frequency in Hz

        except ValueError as e:
            pass

except KeyboardInterrupt as e:
    print('\nReceived Ctrl+c ->Quitting...')
    pass

p.stop()
GPIO.cleanup()
print('I am exiting')