# HTML to JSON Data Extraction

This script extracts structured data from HTML files containing historical property records from the Medford Historical Commission and converts them to JSON format.

## What it does

The script processes HTML files that contain:
- Property information (address, historic name, construction date, etc.)
- Metadata (recorder, organization, date)
- Images (photographs and maps)
- Architectural descriptions
- Historical narratives
- Bibliographies

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the extraction script:
```bash
python extract_tables.py
```

## Output

The script creates a `json_data/` subdirectory containing:

- Individual JSON files for each property (e.g., `HillsideAve_16.json`)
- A combined file `all_properties.json` with all properties

## JSON Structure

Each property JSON file contains:

```json
{
  "filename": "HillsideAve_16",
  "file_path": "HillsideAve_16.html",
  "metadata": {
    "recorded_by": "Jennifer B. Doherty",
    "organization": "Medford Historical Commission",
    "date": "March, 2015"
  },
  "property_info": {
    "town_city": "Medford",
    "place": "Medford Square",
    "address": "16 Hillside Avenue",
    "historic_name": "Frank Hervey House",
    "uses": "Present: Single-family Residential",
    "construction_date": "1889-1898",
    "style_form": "Queen Anne end house",
    "architect_builder": "John W. Russell, architect",
    "condition": "Fair",
    "acreage": "0.09 A"
  },
  "images": [
    {
      "src": "media/image1.png",
      "alt": "",
      "style": "width:3.69514in;height:2.46319in"
    }
  ],
  "architectural_description": "...",
  "historical_narrative": "...",
  "bibliography": "..."
}
```

## Notes

- The script automatically detects and processes all HTML files in the current directory (excluding `index.html`)
- Image paths are preserved as they appear in the HTML
- Text is cleaned and normalized (extra whitespace removed, HTML entities converted)
- The script handles variations in table structure across different property files

## Troubleshooting

If you encounter encoding issues, the script uses UTF-8 encoding. Make sure your HTML files are properly encoded.

For any parsing errors, check the console output for specific file names and error messages.
