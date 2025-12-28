#!/usr/bin/python3
from task_02_csv import convert_csv_to_json
import os

print("=== Testing various CSV files ===\n")

# Test 1: Original file
print("Test 1: Original data.csv")
if convert_csv_to_json("data.csv"):
    print("✓ Success")
else:
    print("✗ Failed")

# Test 2: Empty CSV (only headers)
print("\nTest 2: Empty CSV (only headers)")
if convert_csv_to_json("test_empty.csv"):
    with open('data.json', 'r') as f:
        import json
        data = json.load(f)
        print(f"  Result: {len(data)} rows")
else:
    print("✗ Failed")

# Test 3: Single row
print("\nTest 3: Single row CSV")
if convert_csv_to_json("test_single.csv"):
    with open('data.json', 'r') as f:
        import json
        data = json.load(f)
        print(f"  Result: {data}")
else:
    print("✗ Failed")

# Test 4: Non-existent file
print("\nTest 4: Non-existent file")
result = convert_csv_to_json("does_not_exist.csv")
print(f"  Result: {result} (should be False)")

# Cleanup
for file in ["test_empty.csv", "test_single.csv"]:
    if os.path.exists(file):
        os.remove(file)

print("\n=== All tests completed ===")
