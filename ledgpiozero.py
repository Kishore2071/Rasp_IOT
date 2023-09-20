from gpiozero import LED
from time import sleep

# Led blink program using gpiozero module

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)