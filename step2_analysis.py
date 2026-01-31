import pandas as pd
import matplotlib.pyplot as plt

#Load the data we just made
df = pd.read_csv('sensor_data.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

#plotting the Temperature and vibration
fig, ax = plt.subplots(2, 1, figsize = (12, 8), sharex=True)

#Temperature plot
ax[0].plot(df['timestamp'], df['timestamp'], color='blue', label = 'Temperature (°C)')
ax[0].set_title('Industrial Pump Sensors Readings')
ax[0].legend()

#Vibration plot
ax[1].plot(df['timestamp'], df['vibration'], color= 'orange', label ='Vibration (mm/s)')
ax[1].legend()

#Highligh failure in Red

fail_moments= df[df['fail'] == 1]
ax[0].scatter(fail_moments['timestamp'],fail_moments['temperature'], color= 'red', zorder =5)
ax[1].scatter(fail_moments['timestamp'],fail_moments['vibration'], color= 'red', zorder =5)
plt.tight_layout()
plt.show()