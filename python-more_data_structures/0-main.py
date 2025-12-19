#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty matrix:", square_matrix_simple([]))
print("Single row:", square_matrix_simple([[1, 2, 3]]))
print("Negative numbers:", square_matrix_simple([[-1, -2], [3, 4]]))
