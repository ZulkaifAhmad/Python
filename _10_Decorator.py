"""
Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.

"""
import time

def timer (func):
    def wrapper(*args , **kwargs):
        start = time.time()
        func(*args , **kwargs)
        end = time.time()
        print(f"{__name__} run in {end-start}")
    return wrapper

@timer #decorator
def pause (n):
    time.sleep(n)
    print("Pause function run successfully")
    
pause(3)


