print("BARANI_OTA")

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
def ota():
    while True:
        led.value(1)
        sleep(5)
        led.value(0)
        sleep(5)
        print("BARANI")
