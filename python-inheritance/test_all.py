#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

print("Testing all required cases:")
print("=" * 50)

# 1. integer_validator("age", 1)
try:
    bg.integer_validator("age", 1)
    print("✓ integer_validator('age', 1): PASSED")
except Exception as e:
    print(f"✗ integer_validator('age', 1): FAILED - {e}")

# 2. integer_validator("age", (4,))
try:
    bg.integer_validator("age", (4,))
    print("✗ integer_validator('age', (4,)): SHOULD HAVE FAILED!")
except TypeError as e:
    print(f"✓ integer_validator('age', (4,)): {e}")

# 3. integer_validator("age", [3])
try:
    bg.integer_validator("age", [3])
    print("✗ integer_validator('age', [3]): SHOULD HAVE FAILED!")
except TypeError as e:
    print(f"✓ integer_validator('age', [3]): {e}")

# 4. integer_validator("age", True)
try:
    bg.integer_validator("age", True)
    print("✗ integer_validator('age', True): SHOULD HAVE FAILED!")
except TypeError as e:
    print(f"✓ integer_validator('age', True): {e}")

# 5. integer_validator("age", {3, 4})
try:
    bg.integer_validator("age", {3, 4})
    print("✗ integer_validator('age', {{3, 4}}): SHOULD HAVE FAILED!")
except TypeError as e:
    print(f"✓ integer_validator('age', {{3, 4}}): {e}")

# 6. integer_validator("age", None)
try:
    bg.integer_validator("age", None)
    print("✗ integer_validator('age', None): SHOULD HAVE FAILED!")
except TypeError as e:
    print(f"✓ integer_validator('age', None): {e}")
