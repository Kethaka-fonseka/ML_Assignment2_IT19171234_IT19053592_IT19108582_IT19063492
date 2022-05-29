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

# drop the price data from the x axis
x= vehicle_data.drop('Price', axis=1)

# add the price to the y axis
y= vehicle_data['Price']

# define train and test and test data size
x_train_axis, X_test_axis, y_train_axis, y_test_axis = train_test_split(x, y, test_size=0.25)

# print the shape of the axis
print(x_train_axis.shape, X_test_axis.shape)

# define a method to check the accuracy of the models
def model_accuracy(model):
    model.fit(x_train_axis,y_train_axis)
    accuracy = model.score(X_test_axis,y_test_axis)
    print(str(model)+'=>'+str(accuracy))

# use algorithms to select the highest accuracy algorithm
# Linear Regression Algorithm
# Decision Tree Algorithm
# Random Forest Algorithm

# check linear regression accuracy
LinearReg=LinearRegression()
model_accuracy(LinearReg)

# check decision tree accuracy
DecisionTree=DecisionTreeRegressor()
model_accuracy(DecisionTree)

# check random forest accuracy
RandomForest=RandomForestRegressor()
model_accuracy(RandomForest)
