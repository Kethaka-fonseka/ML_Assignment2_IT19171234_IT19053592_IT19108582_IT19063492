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



