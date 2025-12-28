#!/usr/bin/python3
from task_03_xml import serialize_to_xml, deserialize_from_xml
import os

print("=== Comprehensive XML Serialization Tests ===\n")

# Test 1: Basic dictionary
print("Test 1: Basic dictionary")
dict1 = {'name': 'Alice', 'age': '25', 'city': 'Paris'}
serialize_to_xml(dict1, 'test1.xml')
result1 = deserialize_from_xml('test1.xml')
print(f"Original: {dict1}")
print(f"Result:   {result1}")
print(f"Match:    {dict1 == result1}")

# Test 2: Dictionary with numbers (will be converted to strings)
print("\nTest 2: Dictionary with numbers")
dict2 = {'id': 123, 'price': 99.99, 'active': True}
serialize_to_xml(dict2, 'test2.xml')
result2 = deserialize_from_xml('test2.xml')
print(f"Original: {dict2}")
print(f"Result:   {result2}")
print("Note: All values become strings in XML")

# Test 3: Nested structures (simple approach)
print("\nTest 3: More complex dictionary")
dict3 = {
    'person': 'Bob',
    'details': 'Age: 30, City: London',
    'scores': '95,87,92'
}
serialize_to_xml(dict3, 'test3.xml')
result3 = deserialize_from_xml('test3.xml')
print(f"Original: {dict3}")
print(f"Result:   {result3}")

# Test 4: Empty dictionary
print("\nTest 4: Empty dictionary")
dict4 = {}
serialize_to_xml(dict4, 'test4.xml')
result4 = deserialize_from_xml('test4.xml')
print(f"Original: {dict4}")
print(f"Result:   {result4}")

# Test 5: Check XML format
print("\nTest 5: XML file format")
with open('test1.xml', 'r') as f:
    print("test1.xml content:")
    print(f.read())

# Cleanup
for i in range(1, 5):
    filename = f'test{i}.xml'
    if os.path.exists(filename):
        os.remove(filename)

print("\n=== All tests completed ===")
