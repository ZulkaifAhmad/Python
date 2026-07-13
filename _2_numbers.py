
# Numbers in Python 

"""
there are three types of numbers exists : 
- int -> 12 , float -> 12.2 , complex -> 12j + 23 
"""


big_number = 123456789012345678901234567890

# print(big_number ** 20)  # works fine, no overflow , in other languages
# we can't do this but python is numbers frindly 

print(round(big_number)) # this will round you number from big to small 

# in special cases we use decmial instead of float because float give
# small roundon to the numbers like if e.g 
# 0.2 + 0.3 = 0.55555558 -> here it make mistake of writing 8 because of
#rounding the calculation so that's why we use decmial 

from decimal import Decimal
from random import randint ;

payment = Decimal(34.453) 
discount = Decimal(34.5543)

print(f"\ndecimal usage : {payment * discount}\n") 


#type Conversion : 

int("42")        # 42 (string to int)
float("3.14")    # 3.14
int(3.99)        # 3 (truncates, doesn't round!)
round(3.99)      # 4 (rounds properly)
str(100)         # "100"

print(round(3.99)) # roundoff number from 3.99 t 4

#int("3.14")   #  ValueError — can't parse a float string directly as int
int(float("3.14"))  #  3

"""
 Useful Built-in Functions 

| Function      | Meaning              | Example Output |
| ----------    | -------------------- | -------------- |
| `abs(-15)`    | Make number positive | 15             | 
| `max(2,3,7)`  | Largest value        | 7              |
| `min(2,5,7)`  | Smallest value       | 2              |
| `sum([5,5])`    | Total of list        | 10             |
| `pow(2, 10)`  | Power (exponent)     | 1024           |
|`divmod(17 , 5)`| Quotient+Remainder | (3, 2)          |

from math import sqrt, floor, ceil, pi, log, factorial , random , randint

| Function      | Meaning                 | Example Output |
| ------------- | ----------------------- | -------------- |
| `sqrt(16)`    | Square root             | 4.0            |
| `floor(3.7)`  | Round down              | 3              |
| `ceil(3.2)`   | Round up                | 4              |
| `pi`          | Constant π              | 3.14...        |
| `log(7.389)`  | Logarithm               | 2.0            |
| `factorial(5)`| Multiplication sequence | 120            |

"""
from math import sqrt, floor, ceil, pi, log, factorial 
from random import random , randint

print(f"\nsqrt of 16 is : {int(sqrt(16))}")
print(f"\nfloor of 3.7 is : {floor(3.7)}") # 3
print(f"\nceil of 3.1 is : {ceil(3.1)}")
print(f"\nvalue of pi : {pi}\n")

import random

print(random.random())              # ✅ float between 0 and 1
print(random.choice([1, 2, 3]))      # ✅ pick random item
print(random.randint(1, 10))         # ✅ random int in range

# Formatting numbers in Python


n = 23.4453
print(f"\nformating decimal number: {n:,.2f}")

"""
Format Spec Cheatsheet (f-strings)
------------------------------------------------------------
Symbol   Meaning                          Example
------------------------------------------------------------
,        thousands separator              {1000:,}   -> 1,000
.2f      2 decimal places, fixed float     {3.1:.2f}  -> 3.10
%        percentage (x100 + adds %)        {0.5:.1%}  -> 50.0%
d        integer                           {5:d}      -> 5
>10      right-align, width 10             {5:>10}    -> "         5"
<10      left-align, width 10              {5:<10}    -> "5         "
^10      center align, width 10            {5:^10}    -> "    5     "
0>5      zero-pad, width 5                 {5:05}     -> 00005
------------------------------------------------------------
"""

print(f"gpa in % formating: {0.5:.1%}") # gpa in % formating


# this is how to find hexadeciamal , octal , binary
# finding hex , octal , bin of 255 ?

hexadecimal = hex(255)  # '0xff'
octal = oct(255)        # '0o377'
binary = bin(255)       # '0b11111111'

print(f"\nhexadecimal of 255 is : {hexadecimal}")
print(f"\noctal of 255 is : {octal}")
print(f"\nbinary of 255 is : {binary}")


