#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty list:", divisible_by_2([]))
print("Negative numbers:", divisible_by_2([-4, -3, -2, -1, 0]))
print("Single odd:", divisible_by_2([7]))
print("Single even:", divisible_by_2([8]))
