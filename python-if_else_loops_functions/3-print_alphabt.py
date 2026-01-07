#!/usr/bin/python3
output = ""
for letter in range(97, 123):
    if letter != 101 and letter != 113:
        output += chr(letter)
print("{}".format(output), end="")
