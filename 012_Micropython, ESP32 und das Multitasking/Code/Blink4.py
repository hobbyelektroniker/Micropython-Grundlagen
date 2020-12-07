# Gleichzeitiger Blink mit Argumenten 
# mit Multithreading

from machine import Pin
import time
import _thread

rot = Pin(33, Pin.OUT)
gruen = Pin(25, Pin.OUT)
gelb = Pin(32, Pin.OUT)

anzahl = 10

def blink(led,pause):
    for i in range(anzahl):
        led.on()
        time.sleep(pause)
        led.off()
        time.sleep(pause)

_thread.start_new_thread(blink,(rot,1))
_thread.start_new_thread(blink,(gelb,0.5))
_thread.start_new_thread(blink,(gruen,0.25))
   
print("Alles fertig") # Das ist gelogen !!!






