#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

# Дополнительные тесты
print("\n--- Additional tests ---")
print("Empty sets:", only_diff_elements(set(), set()))
print("Same sets:", only_diff_elements({1, 2}, {1, 2}))
print("No common:", only_diff_elements({1, 2}, {3, 4}))
print("Partial overlap:", only_diff_elements({1, 2, 3}, {2, 3, 4}))
