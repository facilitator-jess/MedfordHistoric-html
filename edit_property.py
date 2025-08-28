#!/usr/bin/env python3
"""
Property Editor for Medford Historic Properties

This script helps you add new properties or edit existing ones.
It provides a structured way to input property data and saves it to JSON.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

def load_properties():
    """Load all existing properties."""
    json_file = Path("json_data/all_properties.json")
    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_properties(properties):
    """Save properties back to JSON."""
    json_file = Path("json_data/all_properties.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(properties, f, indent=2, ensure_ascii=False)
    
    # Also save individual file
    if properties:
        latest_property = properties[-1]
        individual_file = Path(f"json_data/{latest_property['filename']}.json")
        with open(individual_file, 'w', encoding='utf-8') as f:
            json.dump(latest_property, f, indent=2, ensure_ascii=False)

def get_input(prompt: str, default: str = "") -> str:
    """Get user input with optional default value."""
    if default:
        response = input(f"{prompt} (default: {default}): ").strip()
        return response if response else default
    return input(f"{prompt}: ").strip()

def edit_property_data(existing_data: Dict[str, Any] = None) -> Dict[str, Any]:
    """Edit or create property data."""
    print("\n📝 Property Information")
    print("-" * 30)
    
    # Basic info
    filename = get_input("Property filename (e.g., HillsideAve_17)", existing_data.get('filename', ''))
    address = get_input("Address", existing_data.get('property_info', {}).get('address', ''))
    historic_name = get_input("Historic name", existing_data.get('property_info', {}).get('historic_name', ''))
    
    # Property details
    style_form = get_input("Architectural style", existing_data.get('property_info', {}).get('style_form', ''))
    construction_date = get_input("Construction date", existing_data.get('property_info', {}).get('construction_date', ''))
    condition = get_input("Condition", existing_data.get('property_info', {}).get('condition', ''))
    architect_builder = get_input("Architect/Builder", existing_data.get('property_info', {}).get('architect_builder', ''))
    uses = get_input("Uses", existing_data.get('property_info', {}).get('uses', ''))
    acreage = get_input("Acreage", existing_data.get('property_info', {}).get('acreage', ''))
    
    # Metadata
    recorded_by = get_input("Recorded by", existing_data.get('metadata', {}).get('recorded_by', ''))
    date = get_input("Record date", existing_data.get('metadata', {}).get('date', datetime.now().strftime("%B, %Y")))
    
    # Create property structure
    property_data = {
        "filename": filename,
        "file_path": f"{filename}.html",
        "metadata": {
            "recorded_by": recorded_by,
            "organization": "Medford Historical Commission",
            "date": date
        },
        "property_info": {
            "town_city": "Medford",
            "place": "Medford Square",
            "address": address,
            "historic_name": historic_name,
            "uses": uses,
            "construction_date": construction_date,
            "style_form": style_form,
            "architect_builder": architect_builder,
            "condition": condition,
            "acreage": acreage
        },
        "images": [],
        "architectural_description": "",
        "historical_narrative": "",
        "bibliography": ""
    }
    
    return property_data

def main():
    """Main function for property editing."""
    print("🏠 Medford Historic Properties - Property Editor")
    print("=" * 50)
    
    properties = load_properties()
    
    while True:
        print("\nChoose an option:")
        print("1. Add new property")
        print("2. Edit existing property")
        print("3. List all properties")
        print("4. Save and exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            # Add new property
            new_property = edit_property_data()
            properties.append(new_property)
            print(f"✓ Added property: {new_property['property_info']['historic_name'] or new_property['property_info']['address']}")
            
        elif choice == "2":
            # Edit existing property
            if not properties:
                print("No properties to edit.")
                continue
                
            print("\nExisting properties:")
            for i, prop in enumerate(properties):
                name = prop['property_info'].get('historic_name') or prop['property_info'].get('address', 'Unknown')
                print(f"{i + 1}. {name}")
            
            try:
                index = int(input("Enter property number to edit: ")) - 1
                if 0 <= index < len(properties):
                    updated_property = edit_property_data(properties[index])
                    properties[index] = updated_property
                    print(f"✓ Updated property: {updated_property['property_info']['historic_name'] or updated_property['property_info']['address']}")
                else:
                    print("Invalid property number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "3":
            # List all properties
            if not properties:
                print("No properties found.")
            else:
                print(f"\nFound {len(properties)} properties:")
                for i, prop in enumerate(properties):
                    name = prop['property_info'].get('historic_name') or prop['property_info'].get('address', 'Unknown')
                    address = prop['property_info'].get('address', 'No address')
                    print(f"{i + 1}. {name} - {address}")
                    
        elif choice == "4":
            # Save and exit
            save_properties(properties)
            print(f"✓ Saved {len(properties)} properties")
            break
            
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
