#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

# Test cases from error message
test_cases = [
    ("age", 0),           # ValueError
    ("age", (4,)),        # TypeError - tuple
    ("age", [3]),         # TypeError - list  
    ("age", True),        # Это bool, но bool наследуется от int в Python!
    ("age", {3, 4}),      # TypeError - set
    ("age", None),        # TypeError - None
]

print("Testing various invalid cases:")
for name, value in test_cases:
    try:
        bg.integer_validator(name, value)
        print(f"  {name}={value}: PASSED (should have failed!)")
    except TypeError as e:
        print(f"  {name}={value}: TypeError: {e}")
    except ValueError as e:
        print(f"  {name}={value}: ValueError: {e}")
    except Exception as e:
        print(f"  {name}={value}: {type(e).__name__}: {e}")

# Special test for bool
print("\nSpecial test for bool:")
print("isinstance(True, int) =", isinstance(True, int))
print("type(True) is int =", type(True) is int)
print("type(True) =", type(True))
