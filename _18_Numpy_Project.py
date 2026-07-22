import numpy as np

# resturats data of 4 years

data = np.array([
    [1, 200 , 300 , 400 , 500], # TKR 
    [2, 400 , 300 , 600 , 900], # KFC
    [3, 100 , 600 , 500 , 1000], # ColdDrink
    [4, 50 , 200 , 1000 , 1500] # Chai
])

# print their total revenu of all years of each 

sum_of_each = np.sum(data[:, 1:] , axis=1) 
# For each row, sum all elements
# [:, 1:] this mean start from 1st colum to last in axis=1 (mean in row wise)

print(sum_of_each);


# print sum of just one year revenu in colum wise mean 
# sum only one colum

sum_of_one_column = np.sum(data[:, 1:2] , axis=0);
print(sum_of_one_column);


# show me minimun Revenu a resturant made a single year

minimun_revenu = np.min(data[:, 1:] , axis=1);
print(minimun_revenu)

# for maximun : 

maximun_revenu = np.max(data[:, 1:] , axis=1);
print(maximun_revenu)

# for finding avg sales per year 

average_sales = np.mean(data[:, 1:] , axis=1)
print(average_sales);