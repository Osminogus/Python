my_list = [3,4,5]
my_dict = {"key1":"value1", "key2":my_list, "key3":"value3"}
print(my_dict["key2"])
my_dict["key4"]=56
print(my_dict)
my_dict.pop("key4")
print(my_dict)