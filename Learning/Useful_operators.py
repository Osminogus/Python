mylist = range(0,10,1)
for num in mylist:
    print (num)


word = "abcdefg"
index_cont = 0

for item in word:
    print(word[index_cont])
    index_cont +=1

for item in enumerate(word):
    print(item)

for index,letter in enumerate(word):
    print(f"index {index} and letter {letter}")

new_list1 = [1,2,3]
new_list2 = ["a","b","c"]

if 2 in new_list1:
    print("yes")

for item in zip(new_list1, new_list2):
    print(item)

aaa = zip(new_list1, new_list2)
print(type(aaa))

from random import shuffle

one_more_list = [1,2,3,4,5,6,7,8,9]
shuffle(one_more_list)
for item in one_more_list:
    print(item)

from random import randint
print (randint(0,100))

i = input("hi")