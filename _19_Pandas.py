# Pandas

import pandas as pd
import numpy as np

array = np.array([1,2,3,4])
print(f"array : \n{pd.Series(array)}")

list = [1,2,3,4,5]
print(f"list : \n{pd.Series(list)}")

dic = {1:2 , "b" : 3 , 0 : 23}
print(f"dictonary : \n{pd.Series(dic)}")
