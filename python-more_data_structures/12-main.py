#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("IV =", roman_to_int("IV"))
print("MCMXCIV =", roman_to_int("MCMXCIV"))  # 1994
print("Invalid input (None):", roman_to_int(None))
print("Invalid input (not string):", roman_to_int(123))
print("Invalid Roman:", roman_to_int("ABC"))
print("Empty string:", roman_to_int(""))
