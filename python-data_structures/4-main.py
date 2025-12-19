#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Negative index:", new_in_list([1, 2, 3], -1, 99))
print("Out of range:", new_in_list([1, 2, 3], 5, 99))
print("Valid replacement:", new_in_list([1, 2, 3], 1, 99))
print("Original list after tests:", my_list)  # Должен остаться неизменным
