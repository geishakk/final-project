# Write your code here :-)
from machine import Pin, PWM
import neopixel
import time
import random

#DC Motor setup
en = PWM(Pin(15))# Motor enable (PWM speed control)
en.freq(1000)
en.duty(500)

IN1 = Pin(12, Pin.OUT)
IN2 = Pin(13, Pin.OUT)

IN1.value(0)
IN2.value(1)# Motor runs forward

#neoPixel setup
NUM_PIXELS = 16
NUM_ACTIVE = 5
PIN_NUM = 26
COLOR = (200, 150, 80)

neopix = neopixel.NeoPixel(Pin(PIN_NUM), NUM_PIXELS)

def clear_strip():
    for i in range(NUM_PIXELS):
        neopix[i] = (0, 0, 0)
    neopix.write()

def random_pattern():
    clear_strip()
    active_indices = random.sample(range(NUM_PIXELS), NUM_ACTIVE)
    for i in active_indices:
        neopix[i] = COLOR
    neopix.write()

while True:
    random_pattern()
    time.sleep(0.2)
