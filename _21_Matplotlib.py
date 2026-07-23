# Matplotlib
import numpy as np
import matplotlib.pyplot as plt
# here pyplot is the collection of functions that make matplotlib work as MATLAB

revenu = np.array([12,43,87])
oldRevenu = np.array([52,53,47])

plt.plot(revenu , oldRevenu , color="green" , marker="o" , linestyle="dashed");

plt.figure(figsize=(4,4)) 
# use to resize the chart. (custom size)

plt.title("Practic chart")
plt.xlabel("x-axies label")
plt.ylabel("y-axies label")

# plt.show()



# multi line chart 

x = np.array([1,2,3,4,5,6,7,8])
d1 = np.array([12,45,23,67,78,45,89,98])
d2 = np.array([42,15,73,87,78,95,99,100])

plt.plot(x,d1 , label="Sales last Month" , marker="o")
plt.plot(x,d2 , label="Sales Current Month" , marker="o")

plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend() # shows the labels as a small box on the chart
# plt.show()

