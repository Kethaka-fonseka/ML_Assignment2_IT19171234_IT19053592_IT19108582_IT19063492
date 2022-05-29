import process as prc
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


# get data from the process file
vehicle_data = prc.vehicle_data

# convert to the data to the binary format
vehicle_data=pd.get_dummies(vehicle_data)

# print the vehicle dat
print(vehicle_data.head(10))

# print data shape
print(vehicle_data.shape)

