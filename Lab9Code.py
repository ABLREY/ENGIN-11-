import RPi.GPIO as GPIO
import time
from datetime import datetime

# Setup
PIN = 0  # GPIO pin number (BCM numbering)
count = 0  # global count variable

# Callback function to run when falling edge is detected
def pulse_detected(channel):
    global count
    count += 1
    print(f"Pulse detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Assuming pull-up resistor

# Setup falling edge detection
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=pulse_detected, bouncetime=200)

try:
    while True:
        time.sleep(60)  # Wait for one minute
        print(f"\nCount in the last minute: {count}\n")
        count = 0  # Reset counter

except KeyboardInterrupt:
    print("Stopping...")
finally:
    GPIO.cleanup()
