import adafruit_bme680
import time
import board

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

now = time.time()
duration = 5
curr = time.ctime()

while time.time() - now < duration: 
    print("Current time:", curr , "\nTemperature: %0.1f C" % bme680.temperature ,  "Gas: %d ohm" % bme680.gas ,  "Humidity: %0.1f %%" % bme680.relative_humidity ,  "Pressure: %0.3f hPa" % bme680.pressure ,  "Altitude = %0.2f meters" % bme680.altitude)
    time.sleep(2)
    
