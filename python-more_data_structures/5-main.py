#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty dict:", number_keys({}))
print("One key:", number_keys({'a': 1}))
print("Multiple keys:", number_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
