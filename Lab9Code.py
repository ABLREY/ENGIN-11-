import RPi.GPIO as GPIO
import time
from datetime import datetime


PIN = 0
count = 0  

def pulse_detected(channel):
    global count
    count += 1
    print(f"Pulse detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

GPIO.setmode(GPIO.BCM)  
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

GPIO.add_event_detect(PIN, GPIO.FALLING, callback=pulse_detected, bouncetime=200)

try:
    while True:
        time.sleep(60)  
        print(f"\nCount in the last minute: {count}\n")
        count = 0  

except KeyboardInterrupt:
    print("Stopping...")
finally:
    GPIO.cleanup()
