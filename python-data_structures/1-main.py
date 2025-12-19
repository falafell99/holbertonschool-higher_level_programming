#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

# Дополнительные тесты
print("Element at index -1 is", element_at(my_list, -1))
print("Element at index 5 is", element_at(my_list, 5))
print("Element at index 0 is", element_at(my_list, 0))
