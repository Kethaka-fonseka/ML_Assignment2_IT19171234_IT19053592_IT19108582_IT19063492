import analize as ppcd

# get the vehicle data from the analize file
vehicle_data = ppcd.vehicle_data

# define the set_brand method to rename the brands in the data set
def set_brand(name):
    if name == 'Honda' or name == 'Toyota' or name == 'BMW' or name == 'Suzuki' or name == 'Mitsubishi':
        return name
    else:
        return 'Other'


# assign the values to the set_brand method
vehicle_data['Brand'] = vehicle_data['Brand'].apply(set_brand)


# define the set_model method to rename the models in the data set
def set_model(name):
    if name == 'Vezel' or name == 'CHR' or name == 'Land Cruiser Prado' or name == 'CRV' or name == 'Vitz' or name == 'Alto' or name == 'Montero' or name == 'Allion':
        return name
    else:
        return 'Other'

# assign the values to the set_model method
vehicle_data['Model'] = vehicle_data['Model'].apply(set_model)
