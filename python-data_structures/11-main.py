#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Negative index:", delete_at([1, 2, 3], -1))
print("Out of range:", delete_at([1, 2, 3], 5))
print("Delete first:", delete_at([1, 2, 3], 0))
print("Delete last:", delete_at([1, 2, 3], 2))
