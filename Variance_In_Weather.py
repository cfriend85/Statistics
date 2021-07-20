import pandas as pd
import numpy as np
from weather_data import london_data

print (london_data.head())
print (london_data.iloc[100:200]) #This prints rows 100-199 in the dataset
print (len(london_data))

temp = london_data['TemperatureC'] #This puts all of the data in the TemperatureC column of london_data into this variable.
average_temp = np.average(temp) #Averages that data
temperature_var = np.var(temp) #Find the variance
print (temperature_var)
temperature_standard_deviation = np.std(temp) #finds standard deviatons
print (temperature_standard_deviation)
june = london_data.loc[london_data["month"] == 6]["TemperatureC"] #this puts all of the temp info for the month of June into this variable
july = london_data.loc[london_data["month"] == 7]["TemperatureC"] #same for July
print (np.mean(june)) #finds the average for the temp of london in June
print (np.mean(july)) #same for July
print (np.std(june)) #finds standard deviations for the temp of London in June
print (np.std(july)) #same for July

for i in range(1, 13): # This will iterate through the table pulling mean and standard deviation from all the months in this range
    month = london_data.loc[london_data["month"] == i]["TemperatureC"]
    print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
    print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")