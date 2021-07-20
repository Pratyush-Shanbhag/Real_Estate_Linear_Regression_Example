import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'real_estate.csv'
redata = pd.read_csv(file_path)

# print list of columns
print(redata.columns)

# ['No', 'transaction_date', 'house_age', 'distance_nearest_MRT_station', 'num_convenience_stores', 'latitude', 'longitude', 'house_price']

# print first 10 rows of data
print(redata.head())

# drop the useless data columns
redata.drop(redata.columns[[0, 5, 6]], axis=1, inplace=True)

# print first 10 rows of data after modification
print(redata.head())

# print subplots
fig, axs = plt.subplots(ncols=4)
num = 0
for col in redata.columns:
	if col != 'house_price':
		sns.scatterplot(x=col, y='house_price', data=redata, ax=axs[num])
		num = num + 1

plt.show()
