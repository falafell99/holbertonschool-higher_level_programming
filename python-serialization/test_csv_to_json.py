#!/usr/bin/python3
from task_02_csv import convert_csv_to_json

# Test 1: Convert existing CSV file
csv_file = "data.csv"
result = convert_csv_to_json(csv_file)

if result:
    print(f"Data from {csv_file} has been converted to data.json")
    
    # Read and display the JSON file
    import json
    with open('data.json', 'r') as f:
        json_data = json.load(f)
        print("\nConverted JSON data:")
        print(json.dumps(json_data, indent=2))
else:
    print(f"Failed to convert {csv_file}")

# Test 2: Try with non-existent file
print("\n" + "="*50 + "\n")
print("Testing with non-existent file...")
result = convert_csv_to_json("non_existent.csv")
print(f"Result for non-existent file: {result}")
