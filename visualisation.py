import pandas as pd
import matplotlib.pyplot as plt

# loading the data
df = pd.read_csv('Sensor1_data.csv')
df['timestamp'] = pd.to_datetime(df['timestamp']) # pd. to_datetime converts string to real time object

#plotting the temperatture and vibration
fig, ax =plt.subplots(2, 1, figsize = (12, 8), sharex = True) # create a plot with 2 rows and 1 column, the plots should have a size of 12x8 inces

#temperature plot
ax[0].plot(df['timestamp'], df['temperature'], color='blue', label = 'Temperature (C)') # on the first plot , draw temperature versus time in blue and call it temperature
ax[0].set_title('Industrial Pump Sensor Readings') # this is the naming of the top subplot
ax[0].legend()

#vibration plot
ax[1].plot(df['timestamp'], df ['vibration'], color ='orange', label ='Vibration (mm/s)')
ax[1].legend()

#Highlight failures in red
fail_moments = df[df['fail']==1]
ax[0].scatter(fail_moments['timestamp'], fail_moments['temperature'], color ='red', zorder=5) # zorder controlls the layering
ax[1].scatter(fail_moments['timestamp'], fail_moments['vibration'], color='red', zorder =5)

plt.tight_layout()# automatically adjust spacing between plots so that nothing overlaps
plt.show()