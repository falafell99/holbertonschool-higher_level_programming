#!/usr/bin/python3
from task_01_pickle import CustomObject
import os

print("=== Comprehensive Pickle Tests ===\n")

# Test 1: Basic serialization/deserialization
print("Test 1: Basic functionality")
obj1 = CustomObject("Alice", 30, False)
obj1.serialize("test1.pkl")
obj2 = CustomObject.deserialize("test1.pkl")
print(f"Original: {obj1.name}, {obj1.age}, {obj1.is_student}")
print(f"Loaded:   {obj2.name}, {obj2.age}, {obj2.is_student}")
print(f"Success: {obj1.name == obj2.name and obj1.age == obj2.age and obj1.is_student == obj2.is_student}")

# Test 2: Error handling for non-existent file
print("\nTest 2: Non-existent file")
result = CustomObject.deserialize("does_not_exist.pkl")
print(f"Result for non-existent file: {result}")
print(f"Success: {result is None}")

# Test 3: Error handling for corrupted file
print("\nTest 3: Corrupted file")
with open("corrupted.pkl", "wb") as f:
    f.write(b"Not a pickle file")
result = CustomObject.deserialize("corrupted.pkl")
print(f"Result for corrupted file: {result}")
print(f"Success: {result is None}")

# Test 4: Multiple objects
print("\nTest 4: Multiple objects")
objects = [
    CustomObject("Bob", 20, True),
    CustomObject("Charlie", 40, False),
    CustomObject("Diana", 35, True)
]

for i, obj in enumerate(objects):
    obj.serialize(f"obj_{i}.pkl")

print("All objects serialized successfully")

# Cleanup
files = ["test1.pkl", "corrupted.pkl"] + [f"obj_{i}.pkl" for i in range(3)]
for file in files:
    if os.path.exists(file):
        os.remove(file)

print("\n=== All tests completed ===")
