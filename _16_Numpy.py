import numpy as np

array = np.array([[1,2,3,4,5] , [1,3,4,5,6]]);
print(array.shape); # [2,5] two rows and 5 colums

zeros = np.zeros((2,6));

print(zeros.ndim) # 2 -> 2 Dimensions

ones = np.ones((3,10));
print(ones.size) # 30 -> total numbers inside

print(ones.dtype)

print("\n\n\n")

identityMatrix = np.eye(5)
# it is a matrix where elements on dignals or 1 and the rest is zeros

print(f"identity Matrix : \n {identityMatrix}")

print(identityMatrix.shape) 
# this will give me number of rows and columns

print(identityMatrix[0]); 
# get first row of the matrix

print(f"slicing : \n{identityMatrix[1:4]}");
# this will give me from 1st indexed row to 4th (4th excluded) till 3rd row

print("\n\n\n");

arrange = np.arange(0,10,2); 
#crete array start from 0 till 10 with 1 step like leave one and render second
#[0 2 4 6 8]
print(arrange);

arrange2 = np.arange(6);
print(arrange2);

newArr = arrange2.reshape(2,3);  # converted to 2d

randNum = np.random.randint(1,10,2); 
# generate 2 random num between 1 to 10 

randFloat = np.random.rand() * 11
#generate random float number from 0 to 11 

print(f"RandNumber : {randNum}")
print(f"RandFloat : {randFloat}")


