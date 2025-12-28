#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

print("Test 1: Basic functionality")
try:
    bg.integer_validator("my_int", 12)
    print("✓ integer_validator('my_int', 12) passed")
except Exception as e:
    print(f"✗ Failed: {e}")

print("\nTest 2: String should fail")
try:
    bg.integer_validator("name", "John")
    print("✗ Should have raised TypeError")
except TypeError as e:
    print(f"✓ Correctly raised TypeError: {e}")

print("\nTest 3: Zero should fail")
try:
    bg.integer_validator("age", 0)
    print("✗ Should have raised ValueError")
except ValueError as e:
    print(f"✓ Correctly raised ValueError: {e}")

print("\nTest 4: Bool should fail")
try:
    bg.integer_validator("age", True)
    print("✗ Should have raised TypeError")
except TypeError as e:
    print(f"✓ Correctly raised TypeError: {e}")

print("\nAll manual tests completed!")
