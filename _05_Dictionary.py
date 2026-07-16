
# Dictonary

dicy = {
    "name" : "Khan" ,
    "age" : 23 
}

#Loops on Dictonary : 

# for key , value in dic.items():
#     print(key , value);
    
# for key in dic : 
#     print(key)

dicy["age"] = "Twenty-two"

#changes inside dic using bracket notation

dicy[0]  = "one"

# this will create new key and value inside dictonary 
# output : {'name': 'Khan', 'age': 'Twenty-two', 0: 'one'}

print(dicy.get("age")); # Twenty-two

print(len(dicy)) # 3




dictionary = {
    "ali" : "student" ,
    "ali Khan" : "Founder"
}

dictionary["Ali Ahamd"] = "CEO"
# added new key , value

print(f"dictionary : {dictionary}");

# dictionary.pop("ali");
# In dictionary if you want to remove something
# you must enter name inside pop()

del dictionary["Ali Ahamd"]
# another way to remove somthing


Copy = {
    1 : 2 ,
    3 : 4
}

inside = Copy.copy();
#this is how to copy one dictonary inside anoter


# Nested dictonary

nested = {
    "class" : "4" ,
    "subjects" : {
        "book1" : "English" ,
        "book2" : "Urdu"
    } ,
    "Room" : "Block C 234"
}

del nested["subjects"]["book1"]
# this is how to deleted nested keys

print(nested)

# SQURES 

squres = {
    x : x**2 for x in range(0,10)
}

# Output : 

# {
# 0: 0, 
# 1: 1, 
# 2: 4, 
# 3: 9, 
# 4: 16, 
# 5: 25,
# 6: 36, 
# 7: 49, 
# 8: 64, 
# 9: 81
# }

print(squres)=

# formKeys 

keys = [1, 2, 3, 4, 5]
default = "Numbers"

new_dictionary = dict.fromkeys(keys, default)
#{1: 'Numbers', 2: 'Numbers', 3: 'Numbers', 4: 'Numbers', 5: 'Numbers'}


print(new_dictionary)
