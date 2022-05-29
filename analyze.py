import collection as clt
import pandas as pd

# get the vehicle data from the collectData file
print(clt.vehicle_data.head())

vehicle_data = clt.vehicle_data

# Print the Vehicle data
print(vehicle_data.head())

# Remove currency name from the price column
vehicle_data['Price'] = vehicle_data['Price'].str.replace(r"[a-zA-Z]", '0')

# Remove the spaces from the price
vehicle_data['Price'] = vehicle_data['Price'].fillna('').str.replace(' ', "")

# Remove the comma from the Price column
vehicle_data['Price'] = vehicle_data['Price'].fillna('').str.replace(',', "").astype(float)


