#!/usr/bin/env python3
"""
Quick Update Script for Medford Historic Properties

This script quickly syncs JSON data to the web application without server management.
Use this for quick updates when you just need to refresh the data.
"""

import shutil
from pathlib import Path

def quick_update():
    """Quickly copy JSON data to the web application."""
    source_dir = Path("json_data")
    dest_dir = Path("medford-historic-web/public/json_data")
    
    if not source_dir.exists():
        print("✗ json_data directory not found")
        return False
    
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)
    
    print("🔄 Quick update: Copying JSON data to web application...")
    
    # Copy all JSON files
    copied_count = 0
    for json_file in source_dir.glob("*.json"):
        dest_file = dest_dir / json_file.name
        shutil.copy2(json_file, dest_file)
        copied_count += 1
        print(f"  ✓ Copied {json_file.name}")
    
    print(f"✅ Updated {copied_count} files successfully!")
    print("💡 The web application will automatically reload with the new data.")
    return True

if __name__ == "__main__":
    quick_update()
