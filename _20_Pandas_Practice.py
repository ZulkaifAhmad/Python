
import pandas as pd 
import numpy as np

file = pd.read_csv("_00_Data/Dating.csv");

# print(file.dropna()); 
# if there is any NaN or empty row element or coloum elemtn it will drop the complete row

print("\n")
# print(file.fillna(0))
# this will fill the missing elements with 0

file.rename(columns={"sales" : "sale"} , inplace=True )

# print(file.rename(columns={"city" : "cities"} ) )
# this will change coloum name parmently in real file
# and without inplace true it just change it termporarly

file.info()
# here it tells me that your sale colum is float type 
# now i am going to convert it into int type 

file.fillna(0 , inplace=True) 
file["sale"] = file["sale"].astype(int)

# this is how we change type of column values 
# but before doing this first fill the missing values
# if not fill the missing values it will give you an error


file.info()

# Two ways to add new Column

file["address_code"] = [2000 + i for i in range(len(file))]
# file["address_code"] = list(range(2000 , 2000 + len(file)));


def fx(a):
    return a + a

file['ones'] = file["id"].apply(fx)

# here it will create new column but in this column we will take each elemtn of
# id column and add with itself and then add inside onces column 


file.to_csv("_00_Data/newDating.csv" , index=False);
# save the change in the form of another file 

newfile = pd.read_csv("_00_Data/Dating.csv")

# print(newfile)


# Merging : 


d = pd.DataFrame({
    "names" : ["ali" , "ahmad" , "khan"],
    "Marks" : [234 , 423 , 555] 
})

d2 = pd.DataFrame({
    "names" : ["ali" , "ahmad" , "khan"],
    "Rollnumber" : [34 , 43 , 55] 
})

print(pd.concat([d, d2], axis=1))
# concatination , adding two coloums with d or adding d with d2 
#output : 
#    names  Marks  names  Rollnumber
# 0    ali    234    ali          34
# 1  ahmad    423  ahmad          43
# 2   khan    555   khan          55


newDataFrmae = pd.merge(d,d2);
# print(newDataFrmae);

# Output : 
#    names  Marks  Rollnumber
# 0    ali    234          34
# 1  ahmad    423          43
# 2   khan    555          55

