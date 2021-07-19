import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'real_estate.csv'
redata = pd.read_csv(file_path)

print(redata.columns)

print(redata.head())

#['No', 'transaction_date', 'house_age', 'distance_nearest_MRT_station', 'num_convenience_stores', 'latitude', 'longitude', 'house_price']

redata.drop(redata.columns[[0, 5, 6]], axis=1, inplace=True)

print(redata.head())


