#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

# Дополнительные тесты
print("\n--- Test with empty matrix ---")
print_matrix_integer([[]])

print("\n--- Test with different row lengths ---")
matrix2 = [
    [1],
    [2, 3],
    [4, 5, 6]
]
print_matrix_integer(matrix2)
