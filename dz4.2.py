my_list = [3, 4, 5, 2, 2, 7, 4]
if my_list:
    sum_element = sum(my_list[i] for i in range(0, len(my_list), 2))
    last_elements = my_list[-1]
    result = sum_element * last_elements
else:
    result = 0
print(result)
