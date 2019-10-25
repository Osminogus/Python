t = ("door","apple","book","book")
my_list = [1,2,3]
print(type(t))
print(type(my_list))
print(len(t))
print(len(my_list))
print(t[1])
# можно посчитать сколько одинаковых элементов в списке
print(t.count("book"))

# можно определить вхождение первого элемента по заданным параметрам
print(t.index("book"))