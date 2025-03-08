# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside = pd.read_csv('Sensors.csv',skiprows=1)
roof = pd.read_csv('datadiff.csv',skiprows=1)

# %%
display(outside)

# %%
display(roof)

# %%

outside_temp = outside["Temperature (C)"]
outside_humidity = outside["Humidity (%)"]

roof_temp = roof["Temperature (C)"]
roof_humidity = roof["Humidity (%)"]


plt.figure(figsize=(8, 6))
plt.scatter(outside_temp, outside_humidity, label="Outside", alpha=0.5, color="blue")
plt.scatter(roof_temp, roof_humidity, label="Roof", alpha=0.5, color="red")

# Labels and title
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Temperature vs. Humidity Comparison")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


# %%
print("There is a strong negative linear correlation between temperature and humidity in both datasets. This means as temperature increases, humidity decreases, and vice versa.")

# %%
# Create a figure for Temperature vs Gas Resistance
plt.figure(figsize=(10, 5))

# Plot Outside Data
plt.scatter(outside_temp, outside["Gas (ohm)"], alpha=0.5, color="blue", label="Outside")

# Plot Roof Data
plt.scatter(roof_temp, roof["Gas (ohm)"], alpha=0.5, color="red", label="Roof")

# Labels and Title
plt.xlabel("Temperature (°C)")
plt.ylabel("Gas Resistance (Ohm)")
plt.title("Temperature vs Gas Resistance")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


# %%

plt.figure(figsize=(10, 5))

# Plot Outside Data
plt.scatter(outside_temp, outside["PM2.5 (standard)"], alpha=0.5, color="blue", label="Outside")

# Plot Roof Data
plt.scatter(roof_temp, roof["PM2.5 (standard)"], alpha=0.5, color="red", label="Roof")

# Labels and Title
plt.xlabel("Temperature (°C)")
plt.ylabel("PM2.5 (Standard) [µg/m³]")
plt.title("Temperature vs PM2.5")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


# %%
