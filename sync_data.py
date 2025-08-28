#!/usr/bin/env python3
"""
Data Synchronization Script for Medford Historic Properties

This script automates the workflow for updating the web application data:
1. Syncs JSON data from html_files/ to json_data/ (if needed)
2. Copies updated JSON data to medford-historic-web/public/json_data/
3. Optionally restarts the development server
"""

import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import List

def run_command(command: List[str], cwd: str = None) -> bool:
    """Run a command and return success status."""
    try:
        print(f"Running: {' '.join(command)}")
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Command completed successfully")
            if result.stdout.strip():
                print(result.stdout)
            return True
        else:
            print(f"✗ Command failed with return code {result.returncode}")
            if result.stderr.strip():
                print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error running command: {e}")
        return False

def sync_json_data():
    """Extract JSON data from HTML files if needed."""
    html_files_dir = Path("html_files")
    json_data_dir = Path("json_data")
    
    if not html_files_dir.exists():
        print("✗ html_files directory not found")
        return False
    
    # Check if we need to extract JSON data
    html_files = list(html_files_dir.glob("*.html"))
    json_files = list(json_data_dir.glob("*.json"))
    
    # If no JSON files exist or HTML files are newer, extract data
    if not json_files or any(
        html_file.stat().st_mtime > json_data_dir.stat().st_mtime 
        for html_file in html_files
    ):
        print("📊 Extracting JSON data from HTML files...")
        if run_command(["python", "extract_tables.py"], cwd="html_files"):
            print("✓ JSON data extraction completed")
            return True
        else:
            print("✗ JSON data extraction failed")
            return False
    else:
        print("✓ JSON data is up to date")
        return True

def copy_json_to_web_app():
    """Copy JSON data to the Next.js web application."""
    source_dir = Path("json_data")
    dest_dir = Path("medford-historic-web/public/json_data")
    
    if not source_dir.exists():
        print("✗ json_data directory not found")
        return False
    
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)
    
    print("📁 Copying JSON data to web application...")
    
    # Copy all JSON files
    copied_count = 0
    for json_file in source_dir.glob("*.json"):
        dest_file = dest_dir / json_file.name
        shutil.copy2(json_file, dest_file)
        copied_count += 1
        print(f"  ✓ Copied {json_file.name}")
    
    print(f"✓ Copied {copied_count} JSON files to web application")
    return True

def start_dev_server():
    """Start the Next.js development server."""
    web_app_dir = Path("medford-historic-web")
    if not web_app_dir.exists():
        print("✗ medford-historic-web directory not found")
        return False
    
    print("🚀 Starting Next.js development server...")
    
    # Kill any existing dev server
    try:
        subprocess.run(["taskkill", "/f", "/im", "node.exe"], capture_output=True)
        time.sleep(2)  # Give it time to shut down
    except:
        pass
    
    # Start the dev server
    if run_command(["npm", "run", "dev"], cwd="web_app_dir"):
        print("✓ Development server started successfully")
        print("🌐 Visit http://localhost:3000 to view the application")
        return True
    else:
        print("✗ Failed to start development server")
        return False

def check_dependencies():
    """Check if all required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    # Check if beautifulsoup4 is installed
    try:
        import bs4
        print("✓ beautifulsoup4 is installed")
    except ImportError:
        print("✗ beautifulsoup4 not found. Installing...")
        if not run_command([sys.executable, "-m", "pip", "install", "beautifulsoup4"]):
            return False
    
    # Check if Node.js dependencies are installed
    web_app_dir = Path("medford-historic-web")
    if web_app_dir.exists():
        node_modules = web_app_dir / "node_modules"
        if not node_modules.exists():
            print("📦 Installing Node.js dependencies...")
            if not run_command(["npm", "install"], cwd="web_app_dir"):
                return False
    
    print("✓ All dependencies are ready")
    return True

def main():
    """Main function to orchestrate the data sync workflow."""
    print("🔄 Medford Historic Properties - Data Sync")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Step 1: Sync JSON data
    if not sync_json_data():
        return
    
    # Step 2: Copy JSON data to web app
    if not copy_json_to_web_app():
        return
    
    print("\n✅ Data synchronization completed successfully!")
    
    # Ask user if they want to start the dev server
    response = input("\n🚀 Start development server? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        start_dev_server()
    else:
        print("📝 To start the server manually, run: cd medford-historic-web && npm run dev")

if __name__ == "__main__":
    main()
