'''1.	Create 5 different python objects as following:
●	Python list with string values. (Store it in variable data_labels_1)
●	Python list with integer values. (Store it in variable data_values_1)
●	A numpy array. (Store it in variable series_numpy_array_1)
●	A python dictionary (Store it in variable dict2)
'''
# Python list with string values
data_labels_1 = ["JAVA", "PYTHON", "DART"]

# Python list with integer values
data_values_1 = [10, 20, 30]

# A numpy array
import numpy as np
series_numpy_array_1 = np.array([1.5, 2.5, 3.5])

# A python dictionary
dict2 = {"name": "John", "age": 30, "city": "New York"}

'''2.	Create a new python series that stores the population of 5 various cities as data and name of the cities as indexes from data given below. Store it in variable cities_population.
●	indexes = ['Biratnagar', 'Kathmandu', 'Lalitpur', 'Pokhara', 'Narayangarh']
●	data = [200000, 1600000, 600000, 500000, 350000]
'''
import pandas as pd
indexes = ['Biratnagar', 'Kathmandu', 'Lalitpur', 'Pokhara', 'Narayangarh']
data = [200000, 1600000, 600000, 500000, 350000]
cities_population = pd.Series(data, index=indexes)
print(cities_population)
'''
3.	Create different python series for each question below out of the data above as follows:
●	Using python list data_values_1. What do you observe regarding the indexes?
●	Using python list data_labels_1. What do you observe regarding the datatype of the series?
●	Using data_values_1 as data values and data_labels_1 as indexes
●	Using numpy array series_numpy_array_1.
●	Using numpy array series_numpy_array_1. Set the indexes to data_labels_1.
●	Using python dictionary dict2. What do you observe regarding the indexes?

'''
data_values_1 = [10, 20, 30]
data_labels_1 = ["apple", "banana", "cherry"]
series_numpy_array_1 = np.array([1.5, 2.5, 3.5])
dict2 = {"name": "John", "age": 30, "city": "New York"}

series_from_list_int = pd.Series(data_values_1)
print("Series from data_values_1:\n", series_from_list_int)

series_from_list_str = pd.Series(data_labels_1)
print("\nSeries from data_labels_1:\n", series_from_list_str)

series_with_labels = pd.Series(data_values_1, index=data_labels_1)
print("\nSeries with data_labels_1 as indexes:\n", series_with_labels)

series_from_numpy = pd.Series(series_numpy_array_1)
print("\nSeries from numpy array:\n", series_from_numpy)

series_numpy_with_labels = pd.Series(series_numpy_array_1, index=data_labels_1)
print("\nSeries from numpy array with data_labels_1 as indexes:\n", series_numpy_with_labels)

series_from_dict = pd.Series(dict2)
print("\nSeries from dict2:\n", series_from_dict)

# Fetch the indexes of the series cities_population.

indexes_of_cities_population = cities_population.index
print(indexes_of_cities_population)
