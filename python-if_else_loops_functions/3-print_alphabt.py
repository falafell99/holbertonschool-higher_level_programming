#!/usr/bin/python3
for letter in range(97, 123):
    if letter != 101 and letter != 113:  # пропускаем 'e' (101) и 'q' (113)
        print(chr(letter), end="")
print()
