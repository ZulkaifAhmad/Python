import matplotlib.pyplot as plt
import pandas as pd

# Bar chart 

x=[1,2,3,4,5,6]
y=[77,42,13,89,66,59]
z=[87,12,33,49,96,29]
plt.bar(x,y , label="Chai sale last month" , color="yellow" , width=.5)
plt.bar(x,z , label="Chai sale Current month" , color="red" , width=.5)
plt.xlabel("days")
plt.ylabel("Sales")
plt.legend()
plt.title("Chai Revenu Chart")
plt.show()


categories = ["biscut" , "Chai_leaves" , "cold Drink" , "Powder" , "Serfixal"]
sales = [15 , 30 , 45 , 15 , 5]

plt.pie(sales , labels=categories , autopct="%1.1f%%");
plt.title("Shop Sales Last Week");
plt.show()


# scatter plot 

sca = [1,2,3,4,5,6]
sca2 = [12,43,23,54,65,98]


plt.scatter(1,1,1)
plt.plot(sca , sca2)
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend("Chai-Sales")
plt.title("Chai sales")

cat = ["mon" , "tue" , "wed" , "tur"]
sal = [12,23,34,45]
plt.subplot(1,2,1)
plt.scatter(cat , sal);
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend("Powder-Sales")
plt.title("Powder sales")


plt.show()


# making charts with Pandas

dataFrame = pd.DataFrame({
    "days" : ["1st" , "2nd" , "3rd"] ,
    "Sales" : [12,43,56]
})

plt.bar(dataFrame["days"] , dataFrame["Sales"] , label="Shop Sales");
plt.title("Bar with Pandas Data");
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend();
plt.savefig("Shop_Sales.png") # save chart in png form
plt.show();