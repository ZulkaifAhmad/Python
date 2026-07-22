import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,4,5,6]);

print(f"Addition : {a + b}")
print(f"Multiplication : {a * b}")
print(f"subtraction : {a - b}")
print(f"Division : {a / b}")
print(f"Power : {a ** b }")

print(f"Single Array Addition : {a + 10} ") 
# adding 10 with each element of array

# Comparing Numbers 

c = np.array([1,2,3,4,5,6]);
print(f"array<4 : {c<4}") #[ True  True  True False False False]

print(c[c<4],"\n\n") # print those number how is less then 4
# output : [1,2,3];



arr = np.array([1,2,3]);

print(arr.sum()) # sum of all numbers inside array
print(arr.mean()) # average
print(arr.min()) # 1
print(arr.max()) # 3


unordered = np.array([2,3,5,6,1,0,9,7])

print(np.sort(unordered)); 
# will ordered array from assending order

concat = np.concatenate([c,arr]);
print(f"concatinate : {concat}");

#output : [1 2 3 4 5 6 1 2 3]


scores = np.array([78, 85, 90, 45, 67, 88, 92, 55])

print("Average score:", scores.mean())
print("Highest score:", scores.max())
print("Lowest score:", scores.min())
print("Passing scores (>=50):", scores[scores >= 50])
