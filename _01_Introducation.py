inputs = input("Hello World! Please enter your name: "); 
# type  : str

inputs = float(inputs) 
# type casting , explicit type conversion

print(f"Hello {inputs}! Welcome to the program.") 
# updated way to write pyton variables inside str

print(type(inputs))
# float 

x = 23 ;

y = 34.3 ;

print(x + y) ; # type : float 

"""
just for calculation the python covert the x type into float
otherwise if you check the x type individule from y it will give you int
so this is called implicit type conversion


Mutable and Immutable in Python : 

Mutable: A data type whose value can be changed after creation, without creating a new object in memory. The object is modified in place, and its memory address (id) stays the same.
e.g :   list , dict , set , bytearray

Immutable: A data type whose value cannot be changed after creation. Any modification creates a brand new object in memory with a different address, while the original object becomes unreferenced and is eventually cleared by Python's garbage collector.
e.g :   int , float , complex , str , bool , tuple , frozenset , bytes

"""

# Immutable examples
x = 10
x = x + 1        # new int object created

s = "hi"
s = s + " there" # new str object created

t = (1, 2, 3)
# t[0] = 5        # ❌ Error — tuples can't be changed

# Mutable examples
lst = [1, 2, 3]
lst.append(4)     # same list object, modified in place

d = {"a": 1}
d["b"] = 2        # same dict object, modified in place

st = {1, 2}
st.add(3)         # same set object, modified in place



"""
Data Types : 

IMMUTABLE DATA TYPES
---------------------
int          x = 10
float        x = 10.5
complex      x = 3 + 4j
str          x = "hello"
bool         x = True
tuple        x = (1, 2, 3)
frozenset    x = frozenset({1, 2, 3})
bytes        x = b"hello"
range        x = range(5)
NoneType     x = None


MUTABLE DATA TYPES
-------------------
list         x = [1, 2, 3]
dict         x = {"key": "value"}
set          x = {1, 2, 3}
bytearray    x = bytearray(5)

"""

# Diffrence between repr(), str(), print() ,
#  `__repr__()` and id() in python

result = 1/3.0
print(result)          # 0.3333333333333333
print(str(result))     # 0.3333333333333333
print(repr(result))    # 0.3333333333333333
print(id(result))      # memory address of the result object
