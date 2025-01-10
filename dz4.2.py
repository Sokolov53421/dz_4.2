my_list = [3, 4, 5, 2, 2, 7, 4]
if my_list:
    list_1 = sum(my_list[i] for i in range(0, len(my_list), 2))
    elements_list = my_list[-1]
    result = list_1 * elements_list
else:
    result = 0
print(result)
