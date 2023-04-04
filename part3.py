#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pip', 'install pandas')
get_ipython().run_line_magic('pip', 'install seaborn')


# In[ ]:


get_ipython().run_line_magic('pip', 'install boto3')


# In[29]:


import pandas as pd
import seaborn as sns
import boto3
from io import StringIO
from matplotlib import pyplot as plt


# In[30]:


client = boto3.client("iotanalytics")
datasetname = "lab4part3_dataset"
dataset = client.get_dataset_content(datasetName = datasetname)
df = pd.read_csv(dataset['entries'][0]['dataURI'])
i = 0
fig, ax = plt.subplots()
plt.plot(df['timestep_time'],df['vehicle_CO'],marker = "o", markerfacecolor = "blue",label='CO')
plt.plot(df['timestep_time'],df['vehicle_CO2'],marker = "x", markerfacecolor = "red",label='CO2')
plt.xlabel("time")
plt.ylabel('vehicle'+str(i)+' emission')
plt.legend()

fig2, ax2 = plt.subplots()
plt.plot(df['vehicle_speed'],df['vehicle_CO'],marker = "o", markerfacecolor = "blue",label='CO')
plt.plot(df['vehicle_speed'],df['vehicle_CO2'],marker = "x", markerfacecolor = "red",label='CO2')
plt.xlabel("vehicle_speed")
plt.ylabel('vehicle'+str(i)+' emission')
plt.legend()

fig2, ax2 = plt.subplots()
plt.plot(df['vehicle_speed'],df['vehicle_noise'],marker = "o", markerfacecolor = "green",label = 'noise')
plt.xlabel("vehicle_speed")
plt.ylabel('vehicle'+str(i)+' noise level')
plt.legend()


# In[ ]:




