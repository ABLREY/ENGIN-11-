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
        
