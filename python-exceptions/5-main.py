#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

# Дополнительные тесты
print("\n--- Additional tests ---")
try:
    raise_exception()
    print("This should not print")
except TypeError:
    print("Caught TypeError as expected")
except Exception as e:
    print(f"Caught different exception: {type(e).__name__}")
