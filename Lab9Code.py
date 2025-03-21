# coding=utf-8

import RPi.GPIO as GPIO
import datetime
import time
import threading

count = 0
lock = threading.Lock()

# Callback function for falling edge detection
def my_callback(channel):
    global count
    with lock:
        count += 1
    print('▼ Pulse detected at ' + str(datetime.datetime.now()))

def count_printer():
    global count
    while True:
        time.sleep(60)
        with lock:
            print(f"\n=== Total pulses in last minute: {count} ===\n")
            count = 0  # Reset for next minute

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(O, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up resistor assumed
    GPIO.add_event_detect(0, GPIO.FALLING, callback=my_callback, bouncetime=200)

    threading.Thread(target=count_printer, daemon=True).start()

    input('\nPress Enter to exit.\n')

finally:
    GPIO.cleanup()

print("Goodbye!")
