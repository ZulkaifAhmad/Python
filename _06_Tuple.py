"""
Tuple is an ordered and immutable collection used to store
multiple items in a single variable.
It is defined using parentheses ( ), and once a tuple is created,
its elements cannot be changed or modified.
"""

firstTuple = (3,2,4,1,1)

print(firstTuple.count(1))

print(firstTuple[1:]) 

# it will skip 0th number and start form 2nd

print(len(firstTuple))

colors = ("green" , "blue" , "black")

(green , blue , black) = colors # destructuring

print(green) # this will print green.

print(type(green)) #str

print(type(colors)) #tuple

