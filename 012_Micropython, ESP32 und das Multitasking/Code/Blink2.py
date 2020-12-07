# Einfacher Blink mit Argumenten
# ohne Multithreading

from machine import Pin
import time

rot = Pin(33, Pin.OUT)
gruen = Pin(25, Pin.OUT)
gelb = Pin(32, Pin.OUT)

anzahl = 5

def blink(led,pause):
    for i in range(anzahl):
        led.on()
        time.sleep(pause)
        led.off()
        time.sleep(pause)
  
blink(rot,1)
blink(gelb,0.5)
blink(gruen,0.25)





