# coding=utf-8

import RPi.GPIO as GPIO
import datetime
import time
import threading

PIN = 17 
count = 0
lock = threading.Lock()

def my_callback(channel):
    global count
    with lock:
        count += 1
    print('▼ Count detected at ' + str(datetime.datetime.now()))

def count_printer():
    global count
    while True:
        time.sleep(60)
        with lock:
            print(f"\n=== Total counts in last minute: {count} ===\n")
            count = 0  

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
    GPIO.add_event_detect(PIN, GPIO.FALLING, callback=my_callback, bouncetime=1)

    threading.Thread(target=count_printer, daemon=True).start()
    input("Press Enter to exit...\n")

finally:
    GPIO.cleanup()
