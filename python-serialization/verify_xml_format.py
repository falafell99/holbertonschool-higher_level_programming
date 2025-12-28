#!/usr/bin/python3
import xml.etree.ElementTree as ET

# Проверяем формат data.xml
print("=== Checking XML format ===")

# Читаем и показываем XML
with open('data.xml', 'r') as f:
    content = f.read()
    print("XML content:")
    print(content)

# Проверяем структуру
tree = ET.parse('data.xml')
root = tree.getroot()

print("\nXML structure:")
print(f"Root tag: {root.tag}")

print("\nChild elements:")
for child in root:
    print(f"  <{child.tag}> {child.text} </{child.tag}>")

# Преобразуем обратно в словарь
result = {}
for child in root:
    result[child.tag] = child.text

print(f"\nDeserialized dictionary: {result}")

# Ожидаемый результат
expected = {'name': 'John', 'age': '28', 'city': 'New York'}
print(f"Expected: {expected}")
print(f"Match: {result == expected}")
