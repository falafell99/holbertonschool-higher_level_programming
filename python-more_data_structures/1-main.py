#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty list:", search_replace([], 2, 89))
print("No matches:", search_replace([1, 3, 5], 2, 89))
print("All matches:", search_replace([2, 2, 2], 2, 89))
print("String elements:", search_replace(['a', 'b', 'a'], 'a', 'c'))
