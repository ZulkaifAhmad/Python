
# List

my_first_list = [1, 2, 3, 4, 5]

#slicing :

my_first_list[2:]
# print from 2nd index till to end

my_first_list[0:5:2] 
# 1,3,5 -> jump by 1 element

my_first_list[0] = 0; # changes using index
# change (due to mutable)

my_first_list[0:] = [0,1,2,3,4] #changes using slicing
#output will be [0,1,2,3,4]

#trick 
my_list = ["hello" , "world"];
my_list[1:1] = ["test"]
# result : ['hello', 'test', 'world']

my_list[1:2] = []
# output will : delete test element

# print(my_list) 

#conditions and Loops 

list = ["chai" , "apple" ]

for li in list : 
    print(li);
# will print all elements inside list

#conditional rendering 

for li in list : 
    if li.startswith("c") :
        print(li);
# now it will print elements only starts-with c character


list.append("vegitables");
# this will add vegitables in last of list

if "vegitables" in list :
    print("hence proved apple exists" , True)
    

x = ["hello" , "world"];
y = x ; 
# here i just give refrence of x not fully copy x inside y

y.pop();
# print(f"y,{y}"); #["hello"]
# print(f"x,{x}"); #["hello"]

w = ["mirror" , "flag"]
m = w.copy();
# correct way to copy one list inside another

m.remove("flag")
# you can use pop() to remove from last and also can 
# use remove()-> but inside remove you must specifiy
# which one you want to remove 

# print(f"m{m}")
# print(f"w{w}")

w.insert(0,"glass");
# here i insert glass at 0th index

# print(f"w-> insert : {w}")

# loop inside list

squar_numbers = [x**2  for x in range(0,10)]
# output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# finding length 
print(f"length of square_numberes : {len(squar_numbers)}")


 