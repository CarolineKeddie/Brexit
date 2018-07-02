import pandas as pd
import matplotlib.pyplot as plt

census_data = pd.read_csv('assets/datasets/2008-2012-chi-census.csv')

print census_data.head()
print census_data.shape
print census_data.tail()

abandoned_vehicles = pd.read_csv('assets/datasets/chicago_311_abandoned_vehicles.csv')

print abandoned_vehicles.head()
print abandoned_vehicles.shape

print abandoned_vehicles.groupby('Community Area').count().shape

print abandoned_vehicles['Community Area'].value_counts()
print abandoned_vehicles['Community Area'].isnull().sum()
print abandoned_vehicles['Community Area'].describe()

count_of_vehicles = pd.DataFrame(abandoned_vehicles.groupby('Community Area')['Community Area'].count())

merged = census_data.merge(count_of_vehicles, 
        left_on='Community Area Number', 
        right_index=True, how='inner')

merged['count_abandoned_vehicles'] = merged['Community Area']

merged_ls = merged.loc[(merged['Community Area Number'] == 4.0)]
merged_not_ls = merged.loc[(merged['Community Area Number'] != 4.0)]

fig = plt.figure()
ax1 = plt.subplot(121)
for data, cool_color in zip([merged_ls, merged_not_ls], ['red', 'black']):
	plt.scatter(data['Per Capita Income'].values, 
		data['count_abandoned_vehicles'].values, color=cool_color)
ax2 = plt.subplot(122, sharey=ax1)
for data, cool_color in zip([merged_ls, merged_not_ls], ['red', 'black']):
	plt.scatter(data['Percent Households Below Poverty'].values,
		data['count_abandoned_vehicles'].values, color=cool_color)
ax1.set_ylabel('Count of Abandoned Vehicles')
ax1.set_xlabel('Per Capita Income in $s')
ax2.set_xlabel('% Households Below Poverty')
ax2.set_xlim((0, 50))
plt.suptitle('Community Area Statistics by Abandoned Vehicles')

plt.savefig('template.png')
