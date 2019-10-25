my_string = "Hello world"

my_list = []

for letter in my_string:
    my_list.append(letter)

print (my_list)

my_string2 = "Good by"

# The same as loop
my_list = [letter for letter in my_string2]

print (my_list)

my_list = [num**2 for num in range(1,10) if num >=5]
print (my_list)

my_list =[]

for i in [1,2,3]:
    for y in [10,100,1000]:
        my_list.append(i*y)

print (my_list)

my_list = [i*y for i in [1,2,3] for y in [10,100,1000]]
print(my_list)
