#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty dict:")
print_sorted_dictionary({})

print("\nSingle key:")
print_sorted_dictionary({'zebra': 1, 'apple': 2, 'banana': 3})

print("\nNested dict (should not sort inner dict):")
nested = {'b': {'z': 1, 'a': 2}, 'a': [1, 2, 3]}
print_sorted_dictionary(nested)
