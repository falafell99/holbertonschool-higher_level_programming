#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

print("Testing bool values:")
print("type(True) =", type(True))
print("type(True) is int =", type(True) is int)

try:
    bg.integer_validator("test", True)
    print("True accepted (WRONG!)")
except TypeError as e:
    print(f"True rejected: {e}")

try:
    bg.integer_validator("test", False)
    print("False accepted (WRONG!)")
except TypeError as e:
    print(f"False rejected: {e}")
