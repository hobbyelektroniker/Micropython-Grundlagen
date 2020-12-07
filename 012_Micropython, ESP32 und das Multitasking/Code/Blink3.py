# Gleichzeitiger Blink
# mit Multithreading

from machine import Pin
import time
import _thread

rot = Pin(33, Pin.OUT)
gruen = Pin(25, Pin.OUT)
gelb = Pin(32, Pin.OUT)

anzahl = 10

def blink_rot():
    for i in range(anzahl):
        rot.on()
        time.sleep(1)
        rot.off()
        time.sleep(1)
  
def blink_gelb():
    for i in range(anzahl):
        gelb.on()
        time.sleep(0.5)
        gelb.off()
        time.sleep(0.5)
  
def blink_gruen():
    for i in range(anzahl):
        gruen.on()
        time.sleep(0.25)
        gruen.off()
        time.sleep(0.25)
  
  
_thread.start_new_thread(blink_rot,())
_thread.start_new_thread(blink_gelb,())
_thread.start_new_thread(blink_gruen,())

print("Ich bin noch nicht fertig! Ich beende nur das Hauptprogramm.")





