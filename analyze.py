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

# Remove the KM from the Mileage column
vehicle_data['Mileage'] = vehicle_data['Mileage'].str.replace(' km', '')


# Remove the Comma from the Mileage column
vehicle_data['Mileage'] = vehicle_data['Mileage'].str.replace(',', '')

# Remove the - from the Mileage column and convert it to the float
vehicle_data['Mileage'] = vehicle_data['Mileage'].str.replace('-', '0').astype(float)


# Remove the KM from the Capacity column
vehicle_data['Capacity'] = vehicle_data['Capacity'].str.replace(' cc', '')

# Remove the Comma from the Capacity column
vehicle_data['Capacity'] = vehicle_data['Capacity'].str.replace(',', '')

# Remove the - from the Capacity column
vehicle_data['Capacity'] = vehicle_data['Capacity'].str.replace('-', '0')

# remove the null values from the Capacity column
vehicle_data = vehicle_data.dropna(subset=['Capacity'])
vehicle_data['Capacity'] = pd.to_numeric(vehicle_data['Capacity'], errors='coerce')

# convert to the float
vehicle_data['Capacity'] = vehicle_data['Capacity'].astype(float)

# Print the 'Mileage' column
print(vehicle_data.head(20))

