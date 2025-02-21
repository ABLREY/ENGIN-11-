import sys
import time
import adafruit_bme680

import csv
import serial
from adafruit_pm25.uart import PM25_UART
import board

 #Timer 5 minutes
print(sys.argv)
        
if len(sys.argv) < 2:
  print("Script requires run_time(int) as an input")
  exit()
else:
  run_time = int(sys.argv[1])
        
count = 0
while count < run_time:
  print(count)
  count +=1
  time.sleep(1)




# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)


# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

# Set up the UART connection
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
pm25 = PM25_UART(uart, reset_pin=None)
print("Found PM2.5 sensor, reading data...")

now = time.time()
duration = 5


curr = time.ctime()  
print(f"\rCurrent time: {curr} | Temperature: {bme680.temperature:.1f} C | Gas: {bme680.gas} ohm | Humidity: {bme680.relative_humidity:.1f}% | Pressure: {bme680.pressure:.3f} hPa | Altitude: {bme680.altitude:.2f} meters")
time.sleep(2)
    
