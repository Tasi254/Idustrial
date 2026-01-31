import pandas as pd # import pandas for structured data operations
import numpy as np # import numpy for mathematics
from datetime import datetime, timedelta # for specifying time and also highlighting time differernce

np.random.seed() # makes random numbers reproducable
rows= 50 # In my data I will have 50 rows

start_time =datetime (2025, 10, 1) # specifying the start time stamp

data ={
    'timestamp': [start_time + timedelta(minutes =30*i) for i in range (rows)], # I will be incereasing my time by 30minutes equaling the number of specified rows
    'temperature': np.random.normal (30, 5, rows ), # create a mean temp of 30, lowest 30-5/ highest 30+5 equaling the number of rows that i have
    'vibration': np.random.normal (0.05, 0.002, rows), # generate random vibrational values
    'pressure': np.random.normal(40, 3, rows), # generate rando pressure values
    'rpm': np.random.normal(1100, 100, rows)# generate random rpm values

}

df = pd.DataFrame(data)# put the generated data in a structured table using panda
df['fail']=0 # create a new column called fail and fill it with 0s

#temperature
df.loc[15:24, 'temperature'] += np.linspace (0, 14, 10) # generate 9 numbers starting from 0 and ending at 14, should be evenly spaced
df.loc[19:24, 'fail'] =1 # staring from the 19th row to 24th one, use a value of 1 in the fail column

#.loc helps to locate for example a specific row or a column

#vibration 
df.loc[28:33, 'vibration'] *= 2 # take the vibration data within those rows and multiply by 2
df.loc[30:33, 'fail']= 1

#pressure
df.loc[39:44, 'pressure']  -= 8 # reduce the pressure value from the given rows by 8
df.loc[40:44, 'fail'] =1

#creating the csv file 
df.to_csv ('Sensor1_data.csv', index=False) # do save the data index as a column in the csv file
print (" You have successfully created the Simulated failure")



