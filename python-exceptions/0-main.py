#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty list:", safe_print_list([], 5))
print("String list:", safe_print_list(["a", "b", "c"], 2))
print("Mixed list:", safe_print_list([1, "hello", 3.14], 10))
