# Function 


def sequre(num) :
    return num ** 2 ;

number = sequre(4);

print(number);


# Polymorphism means "same function/operation name, different behavior depending on the type of data." Python handles this naturally since it's dynamically typed.

# Same operator/function behaves differently based on data type
print(len("hello"))        # 5 -> counts characters
print(len([1, 2, 3, 4]))   # 4 -> counts list items

# Same function name works for int, float, string differently

def add(a, b):
    return a + b

print(add(2, 3))           # 5       -> numeric addition
print(add("Py", "thon"))   # "Python" -> string concatenation

# A lambda is a small, unnamed (anonymous) function written in one line. Used for short, throwaway logic — you don't need def for it.

# Normal function
def square(x):
    return x * x

# Same thing as a lambda
square_lambda = lambda x: x * x

print(square(5))         # 25
print(square_lambda(5))  # 25

# Common real use: inside sorted(), map(), filter()
nums = [5, 3, 8, 1]
sorted_nums = sorted(nums, key=lambda x: -x)  # sort descending
print(sorted_nums)  # [8, 5, 3, 1]



# *args in python 

def add_all(*args):
    print(args)          # tuple of all arguments passed
    return sum(args)

print(add_all(1, 2))        # (1, 2) -> 3
print(add_all(1, 2, 3, 4))  # (1, 2, 3, 4) -> 10


# Useful when you don't know in advance how many arguments will be passed.


def user_info(**kwargs):
    print(kwargs)  # dict of key-value pairs

user_info(name="Zulkaif", city="Peshawar", role="developer")
# {'name': 'Zulkaif', 'city': 'Peshawar', 'role': 'developer'}

# You can loop through them
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Zulkaif", age=22)




