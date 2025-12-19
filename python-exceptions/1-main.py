#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Float 3.14:", safe_print_integer(3.14))
print("Float 10.0:", safe_print_integer(10.0))
print("String '123':", safe_print_integer("123"))
print("List [1, 2]:", safe_print_integer([1, 2]))
print("None:", safe_print_integer(None))
