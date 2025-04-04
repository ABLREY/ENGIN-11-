# coding=utf-8

import RPi.GPIO as GPIO
import datetime
import time
import threading

PIN = 17 
count = 0
lock = threading.Lock()

csv_filename = "pm25_sensor_data.csv"

with open(csv_filename, mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)

    # Meta-data line
    csv_writer.writerow(["# PM2.5 Sensor Data - Collected on Raspberry Pi"])
    
    # Write headers if the file is empty
    csv_writer.writerow([
        "Timestamp", "PM1.0 (std)", "PM2.5 (std)", "PM10 (std)",
        "PM1.0 (env)", "PM2.5 (env)", "PM10 (env)",
        "Particles >0.3um", "Particles >0.5um", "Particles >1.0um",
        "Particles >2.5um", "Particles >5.0um", "Particles >10um"
    ])

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
