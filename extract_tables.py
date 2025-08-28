#!/usr/bin/env python3
"""
Extract table data from HTML files and convert to JSON format.
This script processes historical property records from the Medford Historical Commission.
"""

import os
import json
import re
from bs4 import BeautifulSoup
from pathlib import Path

def clean_text(text):
    """Clean and normalize text content."""
    if not text:
        return ""
    # Remove extra whitespace and normalize
    text = re.sub(r'\s+', ' ', text.strip())
    # Remove HTML entities
    text = text.replace('&nbsp;', ' ')
    return text

def extract_table_data(soup):
    """Extract structured data from tables in the HTML."""
    tables = soup.find_all('table')
    data = {
        'metadata': {},
        'property_info': {},
        'images': []
    }
    
    for i, table in enumerate(tables):
        rows = table.find_all('tr')
        
        # Skip empty tables
        if not rows:
            continue
            
        # Check if this is an image table (contains img tags)
        images = table.find_all('img')
        if images:
            for img in images:
                src = img.get('src', '')
                if src:
                    data['images'].append({
                        'src': src,
                        'alt': img.get('alt', ''),
                        'style': img.get('style', '')
                    })
            continue
        
        # Process text-based tables
        table_data = []
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if cells:
                row_data = [clean_text(cell.get_text()) for cell in cells]
                table_data.append(row_data)
        
        if table_data:
            # Try to identify table type based on content
            first_cell = table_data[0][0] if table_data and table_data[0] else ""
            
            if "Recorded by:" in first_cell:
                # Metadata table
                for row in table_data:
                    if len(row) >= 1:
                        text = row[0]
                        if "Recorded by:" in text:
                            data['metadata']['recorded_by'] = text.replace("Recorded by:", "").strip()
                        elif "Organization:" in text:
                            data['metadata']['organization'] = text.replace("Organization:", "").strip()
                        elif "Date:" in text:
                            data['metadata']['date'] = text.replace("Date:", "").strip()
            
            elif "Town/City:" in first_cell:
                # Property information table
                for row in table_data:
                    if len(row) >= 1:
                        text = row[0]
                        if "Town/City:" in text:
                            data['property_info']['town_city'] = text.replace("Town/City:", "").strip()
                        elif "Place:" in text:
                            data['property_info']['place'] = text.replace("Place:", "").strip()
                        elif "Address:" in text:
                            data['property_info']['address'] = text.replace("Address:", "").strip()
                        elif "Historic Name:" in text:
                            data['property_info']['historic_name'] = text.replace("Historic Name:", "").strip()
                        elif "Uses:" in text:
                            data['property_info']['uses'] = text.replace("Uses:", "").strip()
                        elif "Date of Construction:" in text:
                            data['property_info']['construction_date'] = text.replace("Date of Construction:", "").strip()
                        elif "Source:" in text:
                            data['property_info']['source'] = text.replace("Source:", "").strip()
                        elif "Style/Form:" in text:
                            data['property_info']['style_form'] = text.replace("Style/Form:", "").strip()
                        elif "Architect/Builder:" in text:
                            data['property_info']['architect_builder'] = text.replace("Architect/Builder:", "").strip()
                        elif "Exterior Material:" in text:
                            data['property_info']['exterior_material'] = text.replace("Exterior Material:", "").strip()
                        elif "Outbuildings/Secondary Structures:" in text:
                            data['property_info']['outbuildings'] = text.replace("Outbuildings/Secondary Structures:", "").strip()
                        elif "Major Alterations:" in text:
                            data['property_info']['major_alterations'] = text.replace("Major Alterations:", "").strip()
                        elif "Condition:" in text:
                            data['property_info']['condition'] = text.replace("Condition:", "").strip()
                        elif "Moved:" in text:
                            data['property_info']['moved'] = text.replace("Moved:", "").strip()
                        elif "Acreage:" in text:
                            data['property_info']['acreage'] = text.replace("Acreage:", "").strip()
                        elif "Setting:" in text:
                            data['property_info']['setting'] = text.replace("Setting:", "").strip()
            
            elif len(table_data) == 1 and len(table_data[0]) >= 3:
                # Assessor's table (usually has 7 columns)
                if len(table_data[0]) >= 7:
                    data['property_info']['assessors_number'] = table_data[0][0]
                    data['property_info']['usgs_quad'] = table_data[0][2]
                    data['property_info']['area'] = table_data[0][4]
                    data['property_info']['form_number'] = table_data[0][6]
    
    return data

def extract_descriptions(soup):
    """Extract architectural description and historical narrative."""
    descriptions = {
        'architectural_description': '',
        'historical_narrative': '',
        'bibliography': ''
    }
    
    # Find architectural description
    arch_desc_start = soup.find(string=re.compile(r'ARCHITECTURAL DESCRIPTION:', re.IGNORECASE))
    if arch_desc_start:
        # Get all text until the next major section
        current = arch_desc_start.parent
        arch_text = []
        while current and current.next_sibling:
            current = current.next_sibling
            if current.name == 'p' and current.find(string=re.compile(r'HISTORICAL NARRATIVE', re.IGNORECASE)):
                break
            if current.name == 'p':
                text = clean_text(current.get_text())
                if text:
                    arch_text.append(text)
        descriptions['architectural_description'] = ' '.join(arch_text)
    
    # Find historical narrative
    hist_narr_start = soup.find(string=re.compile(r'HISTORICAL NARRATIVE', re.IGNORECASE))
    if hist_narr_start:
        current = hist_narr_start.parent
        hist_text = []
        while current and current.next_sibling:
            current = current.next_sibling
            if current.name == 'p' and current.find(string=re.compile(r'BIBLIOGRAPHY', re.IGNORECASE)):
                break
            if current.name == 'p':
                text = clean_text(current.get_text())
                if text:
                    hist_text.append(text)
        descriptions['historical_narrative'] = ' '.join(hist_text)
    
    # Find bibliography
    bib_start = soup.find(string=re.compile(r'BIBLIOGRAPHY', re.IGNORECASE))
    if bib_start:
        current = bib_start.parent
        bib_text = []
        while current and current.next_sibling:
            current = current.next_sibling
            if current.name == 'p':
                text = clean_text(current.get_text())
                if text:
                    bib_text.append(text)
        descriptions['bibliography'] = ' '.join(bib_text)
    
    return descriptions

def process_html_file(file_path):
    """Process a single HTML file and extract structured data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract basic info from filename
        filename = Path(file_path).stem
        data = {
            'filename': filename,
            'file_path': str(file_path)
        }
        
        # Extract table data
        table_data = extract_table_data(soup)
        data.update(table_data)
        
        # Extract descriptions
        descriptions = extract_descriptions(soup)
        data.update(descriptions)
        
        return data
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    """Main function to process all HTML files."""
    # Create output directory
    output_dir = Path("json_data")
    output_dir.mkdir(exist_ok=True)
    
    # Get all HTML files (excluding index.html)
    html_files = [f for f in Path('.').glob('*.html') if f.name != 'index.html']
    
    print(f"Found {len(html_files)} HTML files to process")
    
    all_data = []
    
    for html_file in html_files:
        print(f"Processing {html_file.name}...")
        data = process_html_file(html_file)
        
        if data:
            # Save individual file
            output_file = output_dir / f"{html_file.stem}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            all_data.append(data)
    
    # Save combined data
    combined_file = output_dir / "all_properties.json"
    with open(combined_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nProcessing complete!")
    print(f"Individual JSON files saved in: {output_dir}")
    print(f"Combined data saved as: {combined_file}")
    print(f"Total properties processed: {len(all_data)}")

if __name__ == "__main__":
    main()
