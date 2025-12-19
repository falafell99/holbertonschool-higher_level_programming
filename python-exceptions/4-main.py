#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Different lengths:", list_division([1, 2], [1, 2, 3], 3))
print("Empty lists:", list_division([], [], 2))
print("Float division:", list_division([1.5, 2.5], [0.5, 0.5], 2))
