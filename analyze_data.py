#!/usr/bin/env python3
"""
Analyze the extracted JSON data and show statistics.
"""

import json
from pathlib import Path
from collections import Counter

def analyze_data():
    """Analyze the extracted property data."""
    
    # Load the combined data
    with open('json_data/all_properties.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Total properties: {len(data)}")
    print()
    
    # Count properties by street
    streets = []
    for prop in data:
        if 'address' in prop.get('property_info', {}):
            address = prop['property_info']['address']
            if address:
                # Extract street name from address
                parts = address.split()
                if len(parts) >= 3:
                    street = ' '.join(parts[2:])  # Skip number and street number
                    streets.append(street)
    
    street_counts = Counter(streets)
    print("Properties by street:")
    for street, count in street_counts.most_common():
        print(f"  {street}: {count}")
    print()
    
    # Count architectural styles
    styles = []
    for prop in data:
        if 'style_form' in prop.get('property_info', {}):
            style = prop['property_info']['style_form']
            if style:
                styles.append(style)
    
    style_counts = Counter(styles)
    print("Architectural styles:")
    for style, count in style_counts.most_common():
        print(f"  {style}: {count}")
    print()
    
    # Count construction dates
    dates = []
    for prop in data:
        if 'construction_date' in prop.get('property_info', {}):
            date = prop['property_info']['construction_date']
            if date:
                dates.append(date)
    
    date_counts = Counter(dates)
    print("Construction dates:")
    for date, count in date_counts.most_common():
        print(f"  {date}: {count}")
    print()
    
    # Count conditions
    conditions = []
    for prop in data:
        if 'condition' in prop.get('property_info', {}):
            condition = prop['property_info']['condition']
            if condition:
                conditions.append(condition)
    
    condition_counts = Counter(conditions)
    print("Property conditions:")
    for condition, count in condition_counts.most_common():
        print(f"  {condition}: {count}")
    print()
    
    # Show properties with images
    properties_with_images = sum(1 for prop in data if prop.get('images'))
    print(f"Properties with images: {properties_with_images}/{len(data)}")
    
    # Show properties with complete descriptions
    properties_with_arch_desc = sum(1 for prop in data if prop.get('architectural_description'))
    properties_with_hist_narr = sum(1 for prop in data if prop.get('historical_narrative'))
    print(f"Properties with architectural descriptions: {properties_with_arch_desc}/{len(data)}")
    print(f"Properties with historical narratives: {properties_with_hist_narr}/{len(data)}")

if __name__ == "__main__":
    analyze_data()
