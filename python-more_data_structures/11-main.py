#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty list:", multiply_list_map([], 5))
print("Number 0:", multiply_list_map([1, 2, 3], 0))
print("Negative number:", multiply_list_map([1, 2, 3], -2))
print("Float number:", multiply_list_map([1.5, 2.5], 2))
