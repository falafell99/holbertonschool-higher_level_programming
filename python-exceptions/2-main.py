#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty list:", safe_print_list_integers([], 5))
print("No integers:", safe_print_list_integers(["a", "b", 3.14], 3))
print("Mixed:", safe_print_list_integers([1, "a", 2, "b", 3, [4]], 6))
