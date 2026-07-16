
string = "chai, aur, code"

print(len(string)); # 15

lowercase = string.lower();
uppercase = string.upper();
split = string.split(", ");
replace = string.replace("chai" , "Tea");

special_Print = string[0:] 
#this will save from starting to the ending 

special_Print_2 = string[1:7:2] 
# this will start from 1th index till to 7(7th char is not included)
# and will skip every one element after one

find_any_char = string.find("c"); 
# this will give us 0 because c exists on index 0
find_any_word = string.find("code");
#this will give us 11 because code word starts from 11th index


# INJECT Variables inside string : 

drink = "chai"
order = 2
statment = "I ordered {} cups of {}";
formate_statment = statment.format(order , drink)
# result = I ordered 2 cups of chai

#how to join a list of strings into a single string

list_of_strings = ["I", "ordered", "2", "cups", "of", "chai"]

join_list = "-".join(list_of_strings) # i made slug here from list

print("ordered" in join_list) # True 
print("ordereds" in join_list) # False 

name = "ali khan"

name.startswith("a") #true
name.endswith("a") #false

