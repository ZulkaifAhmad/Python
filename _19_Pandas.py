import pandas as pd
import numpy as np

# Series : a single column of data (like one list, with labels).

array = np.array([1,2,3,4])
# print(f"array : \n{pd.Series(array)}")

list = [1,2,3,4,5]
# print(f"list : \n{pd.Series(list)}")

dic = {1:2 , "b" : 3 , 0 : 23}
# print(f"dictonary : \n{pd.Series(dic)}")


# Data Frames : a full table made of many columns (like a spreadsheet).


frame = pd.DataFrame({
    "names": ["Zulkaif", "Ali", "Khan"],
    "ages": ["18 Plus", "below 18", "60 Plus"],
    "edu": ["10th" , "12th" , "15th"]
})

# print(frame);


another = pd.DataFrame(
    [
        ["Ali" , 22 , "FSC"] , 
        ["Zulkaif" , 20 , "BS"] ,
        ["Khan" , 30 , "HSSC"]
    ] ,
    columns=["Names" , "Ages" , "Qualification"]
)

# print(another)

df = pd.read_csv("_00_Data/Dating.csv");
# print(df)

#   print(f"df.head() :\n\n {df.head()}")      # shows first 5 rows
#   print(f"df.tail() :\n\n {df.tail()}")      # shows last 5 rows
#   print(f"df.shape :\n\n {df.shape}")       # (rows, columns) -> e.g. (100, 5)
#   print(f"df.columns :\n\n {df.columns}")     # list of column names
#   print(f"df.info() :\n\n {df.info()}")      # column names, types, and missing values
#   print(f"df.describe() :\n\n {df.describe()}")  # quick statistics (average, min, max, etc.) for number columns


# print(type(df["match"]));

# print(df.iloc[1]) 
# this will show you 2nd row with labels

# print(df.loc[0:3]); # slicing


Lahore_sales = df[(df["city"] == "Lahore") & (df["sales"] > 400)];

show_all_Lahore_sales = df[df["city"] == "Lahore"]
print(show_all_Lahore_sales)

