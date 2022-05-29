import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import the data set
vehicle_data = pd.read_csv('vehicle_data.csv')

# We used the below code to reduce the number of records in the data file
# vehicle_data.drop(vehicle_data.index[1001:4123970], inplace=True)

# print the vehicle data sets
print(vehicle_data.tail())

# print the vehicle data Shape
print(vehicle_data.shape)

# print the non null and dtype
print(vehicle_data.info())

# print 2 datas
print(vehicle_data.head(2))

# check null values
print(vehicle_data.isnull())

