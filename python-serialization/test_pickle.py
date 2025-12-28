#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
if new_obj:
    new_obj.display()
else:
    print("Failed to deserialize object")

# Test error handling with non-existent file
print("\nTesting error handling:")
bad_obj = CustomObject.deserialize("non_existent.pkl")
if bad_obj is None:
    print("Correctly returned None for non-existent file")
