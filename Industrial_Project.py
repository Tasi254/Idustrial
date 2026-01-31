import pandas as pd
import numpy as np
from datetime import datetime , timedelta

np.random.seed(42)
rows =5000
start_time =datetime(2023, 1, 1)

data = {
    'timestamp': [start_time + timedelta(minutes=10*i) for i in range (rows)],
    'temperature': np.random.normal(65,5,rows), # mean 65
    'vibration': np.random.normal(0.02, 0.005, rows), # mean 0.02 mm/s
    'pressure': np.random.normal(50, 2, rows), # mean 50 PSI
    'rpm': np.random.normal(1500, 50, rows) # mean 1500 RPM
}


df = pd.DataFrame(data)
# 3. " Inject" Industrial failures ( The Story for conference)
# We will create a failure label. 0=Healthy, 1= Failure
df['fail']= 0

#Scenario A : Heat-related failure (rows 1000 to 1050)
df.loc[1000:1050, 'temperature'] += np.linspace (0, 30, 51)
df.loc[1040:1050, 'fail']=1

# Scenario B: High vibration failure  ( rows 3000 to 3080)
df.loc[3000:3080, 'vibration'] *= 3
df.loc[3070:3080, 'fail']=1

# Scenario C: Pressure drop (row 4500 to 4550)
df.loc[4500:4550, 'pressure'] -= 15
df.loc[4540:4550, 'fail'] = 1

#Save the data to a csv file
df.to_csv ('Sensor_data.csv', index= False)
print(" Success! 'Sensor_data.csv has been created with simulated failure.")