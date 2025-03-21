# coding=utf-8

import RPi.GPIO as GPIO
import datetime
import time
import threading

PIN = 17  # GPIO 17 (BCM numbering)
count = 0
lock = threading.Lock()

# Callback function for falling edge detection
def my_callback(channel):
    global count
    with lock:
        count += 1
    print('▼ Count detected at ' + str(datetime.datetime.now()))

# Threaded function to print count every 60 seconds
def count_printer():
    global count
    while True:
        time.sleep(60)
        with lock:
            print(f"\n=== Total counts in last minute: {count} ===\n")
            count = 0  # Reset for next minute

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use pull-up resistor
    GPIO.add_event_detect(PIN, GPIO.FALLING, callback=my_callback, bouncetime=1)

    # Start background thread to report counts
    threading.Thread(target=count_printer, daemon=True).start()

    # Keep script running — use input() or infinite loop
    input("Monitoring started. Press Enter to exit...\n")

finally:
    GPIO.cleanup()
