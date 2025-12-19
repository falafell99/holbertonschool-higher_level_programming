#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

# Дополнительные тесты
print("Test 2 - negative index:", replace_in_list([1, 2, 3], -1, 99))
print("Test 3 - out of range:", replace_in_list([1, 2, 3], 5, 99))
print("Test 4 - valid replacement:", replace_in_list([1, 2, 3], 1, 99))
