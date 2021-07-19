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

fig, axs = plt.subplots(ncols=4)
num = 0
for col in redata.columns:
	if col != 'house_price':
		sns.scatterplot(x=col, y='house_price', data=redata, ax=axs[num])
		num = num + 1

plt.show()
