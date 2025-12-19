#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Дополнительные тесты
print("Empty list:", max_integer([]))
print("Single element:", max_integer([42]))
print("Negative numbers:", max_integer([-5, -1, -10]))
print("All same:", max_integer([7, 7, 7, 7]))
