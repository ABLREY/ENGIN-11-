import time
import csv
import serial
from adafruit_pm25.uart import PM25_UART

# Set up the UART connection
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
pm25 = PM25_UART(uart, reset_pin=None)

print("Found PM2.5 sensor, reading data...")

# Define output CSV file
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

    print("Logging PM2.5 data for 1 minute...")

    start_time = time.time()  # Start timer

    while time.time() - start_time < 60:  # Run for 60 seconds
        time.sleep(1)

        try:
            aqdata = pm25.read()
        except RuntimeError:
            print("Unable to read from sensor, retrying...")
            continue

        # Get timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Write data to CSV
        csv_writer.writerow([
            timestamp, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"],
            aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"],
            aqdata["particles 03um"], aqdata["particles 05um"], aqdata["particles 10um"],
            aqdata["particles 25um"], aqdata["particles 50um"], aqdata["particles 100um"]
        ])

        # Print collected data
        print()
        print("Concentration Units (standard)")
        print("---------------------------------------")
        print(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
        )
        print("Concentration Units (environmental)")
        print("---------------------------------------")
        print(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
        )
        print("---------------------------------------")
        print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
        print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
        print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
        print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
        print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
        print("Particles > 10um / 0.1L air:", aqdata["particles 100um"])
        print("---------------------------------------")

print(f"Data logging complete! File saved as {csv_filename}")
