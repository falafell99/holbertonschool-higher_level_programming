#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty sets:", common_elements(set(), set()))
print("No common:", common_elements({1, 2}, {3, 4}))
print("All common:", common_elements({1, 2}, {1, 2}))
print("Partial:", common_elements({1, 2, 3}, {2, 3, 4}))
