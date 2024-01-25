# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

######  Example 1.11 ##########
# load text file
fname = 'Sales_01_20.csv' # comma separated values
data1 = np.loadtxt(fname, delimiter=',', skiprows=1)
years = np.unique(data1[:, 0])

mean_sales_by_year = []
for year in years:
    year_sales = data1[data1[:, 0] == year][:, 1] 
    mean_sales = np.mean(year_sales)
    mean_sales_by_year.append(mean_sales)
    print("Mean sales for {}: {}".format(int(year), mean_sales))
for year in years:
    year_sales = data1[data1[:, 0] == year][:, 1]
    std_sales = np.std(year_sales)
for year in years:
    year_data = data1[data1[:, 0] == year]
    pri2030= year_data[(year_data[:, 1] >= 200000) & (year_data[:, 1] <=300000)]
    num_sales_in_range = pri2030.shape[0]
   
   # calculate total number of sales for year
    total_sales_for_year = year_data.shape[0]
   
   # calculate yearly probability
    yearly_prob = num_sales_in_range / total_sales_for_year
    print(f"Year {year}: {yearly_prob:.2%}")
fig, ax = plt.subplots()
ax.bar(years, mean_sales_by_year, width=0.8, edgecolor='black')
ax.set_xlabel('Year')
ax.set_ylabel('Mean Sale Price')
ax.set_title('Histogram of Mean Sale Price by Year')

# set x-tick spacing to every 5 years
ax.set_xticks(np.arange(min(years), max(years)+1, 5))

plt.show()