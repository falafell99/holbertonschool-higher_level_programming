#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("5 / 2 =", safe_print_division(5, 2))
print("-10 / 3 =", safe_print_division(-10, 3))
print("0 / 5 =", safe_print_division(0, 5))
