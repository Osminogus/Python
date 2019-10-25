my_list = ["1", 345, 45.2, ["home", 11.2]]
print(my_list)
my_list[0] = "Sasha"
print(my_list)
my_list.append("the last")
print(my_list[3][1])
# Делаем список из однотипных значений
my_list2=[0]*3
print(my_list2)

my_list3=[0,1,[3,4,"hi",["by",6]]]
# Получаем соответствующее значение по его индексу
print(my_list3[2][3][0])
# Переопределяем значение
my_list3[2][3][0] = "yahoo"
print(my_list3[2][3][0])

