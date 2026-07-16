
# Loops 

# 1. FOR LOOP
# Used to iterate over a sequence (list, string, range, etc.)
# 

# Looping through a range of numbers
for i in range(5):          # range(5) gives 0,1,2,3,4
    print("For loop count:", i)

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Looping through a string (each character)
for char in "hi":
    print("Character:", char)


# 2. WHILE LOOP
# Used when you loop based on a condition being True


count = 0
while count < 5:            # runs as long as condition is True
    print("While loop count:", count)
    count += 1               # important: update the variable or it loops forever



# 3. NESTED LOOP
# A loop inside another loop (works with both for/while)


for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# 4. LOOP CONTROL STATEMENTS

# break -> stops the loop completely
for i in range(10):
    if i == 3:
        break            # exits loop when i is 3
    print("break example:", i)

# continue -> skips current iteration, moves to next
for i in range(5):
    if i == 2:
        continue          # skips printing 2
    print("continue example:", i)

# else with loop -> runs only if loop completes WITHOUT break

for i in range(3):
    print("else example:", i)
else:
    print("Loop finished without break")
    
    