#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

# Дополнительные тесты
print("\n--- Additional tests ---")
try:
    raise_exception_msg("Python is cool")
except NameError as e:
    print(f"Message: {e}")

try:
    raise_exception_msg()  # Пустое сообщение
except NameError as e:
    print(f"Empty message: '{e}'")
