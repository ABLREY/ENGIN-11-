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

while time.time() - now < duration: 
    curr = time.ctime()  
    print(f"\rCurrent time: {curr} | Temperature: {bme680.temperature:.1f} C | Gas: {bme680.gas} ohm | Humidity: {bme680.relative_humidity:.1f}% | Pressure: {bme680.pressure:.3f} hPa | Altitude: {bme680.altitude:.2f} meters")
    time.sleep(2)
    
