# Conditions
my_string = "try"
if my_string =='hi':
    print(my_string)
elif my_string =="try":
    print("try")
else:
    print("by")

# Loop
my_list = [45,35,57,36]
for item_name in my_list:
    print (item_name)

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print (f"Четное число: {number}")
    else:
        print (f"Нечетное число: {number}")

#=========================
new_list = [(1,2),(3,4),(5,6),(7,8)]

for (var1,var2) in new_list:
    print(var1)


#====Dictionary++++++
my_dict = {"key1":"bla-bla","key2":"tratata","key3":"omom"}

for key,value in my_dict.items():
    print(key)
    print(value)

x=0
while x<=10:
    print (f"это икс {x}")
    x +=1
else:
    print ("Конец")

x = [1,2,3,4,5,6]

for item in x:
    pass

for item in "Привет это я":
    if item=="П" or item == "р":
        continue
    elif item =="э":
        break
    print(item)