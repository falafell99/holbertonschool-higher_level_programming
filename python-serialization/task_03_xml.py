#!/usr/bin/python3
"""Serialize and deserialize data using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML file.

    Args:
        dictionary (dict): Python dictionary to serialize
        filename (str): Name of the XML file to create
    """
    try:
        # Create root element
        root = ET.Element("data")
        
        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convert all values to strings
        
        # Create element tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        raise


def deserialize_from_xml(filename):
    """
    Deserialize XML file to Python dictionary.

    Args:
        filename (str): Name of the XML file to read

    Returns:
        dict: Deserialized Python dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct dictionary from XML elements
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return {}
