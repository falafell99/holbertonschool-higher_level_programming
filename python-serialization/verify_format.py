#!/usr/bin/python3
import json

# Результат должен быть ТОЧНО таким:
expected = [
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"},
    {"name": "Bob", "age": "22", "city": "Chicago"},
    {"name": "Eve", "age": "30", "city": "San Francisco"}
]

with open('data.json', 'r') as f:
    actual = json.load(f)

print("Expected:", json.dumps(expected, indent=2))
print("\nActual:", json.dumps(actual, indent=2))
print("\nMatch:", expected == actual)

# Важно: в CSV все значения строковые, поэтому age тоже строки
print("\nCheck data types:")
for i, item in enumerate(actual):
    print(f"Row {i}:")
    for key, value in item.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")
