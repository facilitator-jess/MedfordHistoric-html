# Medford Historic Properties - Workflow Guide

This guide explains the different workflows for managing property data in the Medford Historic Properties project.

## 🚀 Quick Start Workflow

### For New Users / Full Setup
```bash
# Run the full sync script (install dependencies, extract data, copy to web app)
python sync_data.py
```

### For Regular Development
```bash
# 1. Start the development server (if not already running)
cd medford-historic-web
npm run dev

# 2. Make changes to data (see workflows below)

# 3. Quick update to see changes
python quick_update.py
```

## 📝 Data Management Workflows

### Workflow 1: Adding/Editing Properties via Script

1. **Run the property editor:**
   ```bash
   python edit_property.py
   ```

2. **Choose options:**
   - Option 1: Add new property
   - Option 2: Edit existing property
   - Option 3: List all properties
   - Option 4: Save and exit

3. **Update the web application:**
   ```bash
   python quick_update.py
   ```

### Workflow 2: Manual JSON Editing

1. **Edit JSON data directly:**
   ```bash
   # Edit individual property
   notepad json_data/HillsideAve_16.json
   
   # Or edit the combined file
   notepad json_data/all_properties.json
   ```

2. **Sync to web application:**
   ```bash
   python quick_update.py
   ```

### Workflow 3: Adding New HTML Files

1. **Add new HTML files to `html_files/`:**
   ```bash
   # Copy new HTML files here
   cp new_property.html html_files/
   ```

2. **Extract JSON data:**
   ```bash
   cd html_files
   python extract_tables.py
   cd ..
   ```

3. **Sync to web application:**
   ```bash
   python quick_update.py
   ```

## 🔧 Available Scripts

### `sync_data.py` - Full Sync Script
- Checks dependencies
- Extracts JSON from HTML files (if needed)
- Copies JSON to web application
- Optionally starts development server

**Use when:** Setting up for the first time or after major changes

### `quick_update.py` - Quick Update Script
- Quickly copies JSON data to web application
- No dependency checks or server management

**Use when:** You've made small changes and just need to refresh the web app

### `edit_property.py` - Property Editor
- Interactive property editor
- Add new properties
- Edit existing properties
- Save changes automatically

**Use when:** Adding new properties or editing property details

## 📁 File Structure

```
MedfordHistoric-html/
├── html_files/                    # Original HTML files
│   ├── *.html                     # Property HTML files
│   └── extract_tables.py          # Data extraction script
├── json_data/                     # Extracted JSON data
│   ├── *.json                     # Individual property files
│   └── all_properties.json        # Combined dataset
├── medford-historic-web/          # Next.js web application
│   └── public/json_data/          # JSON data for web app
├── sync_data.py                   # Full sync script
├── quick_update.py                # Quick update script
├── edit_property.py               # Property editor
└── WORKFLOW_GUIDE.md              # This file
```

## 🎯 Common Scenarios

### Scenario 1: Adding a New Property
```bash
# Option A: Use property editor
python edit_property.py
# Choose option 1, fill in details, save

# Option B: Add HTML file and extract
cp new_property.html html_files/
cd html_files && python extract_tables.py && cd ..

# Sync to web app
python quick_update.py
```

### Scenario 2: Editing Existing Property
```bash
# Option A: Use property editor
python edit_property.py
# Choose option 2, select property, edit, save

# Option B: Edit JSON directly
notepad json_data/HillsideAve_16.json

# Sync to web app
python quick_update.py
```

### Scenario 3: Updating Multiple Properties
```bash
# Edit JSON files directly
# ... make changes ...

# Sync all changes
python quick_update.py
```

### Scenario 4: Starting Fresh Development Session
```bash
# Full sync (recommended)
python sync_data.py

# Or manual approach
cd medford-historic-web
npm run dev
```

## 💡 Tips and Best Practices

1. **Always run `quick_update.py` after making data changes**
   - This ensures the web application sees your changes
   - The web app will automatically reload

2. **Use `edit_property.py` for structured editing**
   - Ensures consistent data format
   - Prevents JSON syntax errors
   - Provides validation

3. **Keep HTML files in sync**
   - If you add new HTML files, re-run extraction
   - This maintains data integrity

4. **Check the web application**
   - Always verify changes appear correctly
   - Test search and filter functionality

5. **Backup your data**
   - JSON files contain all your work
   - Consider version control for data files

## 🚨 Troubleshooting

### Images not showing
- Check that image paths in JSON are correct
- Images should be in `html_files/media/`
- Copy media folder to `medford-historic-web/public/` if needed

### Web app not updating
- Run `python quick_update.py`
- Check that JSON files are valid
- Restart development server if needed

### Property editor not working
- Ensure `json_data/all_properties.json` exists
- Check file permissions
- Verify Python dependencies are installed

## 📞 Getting Help

If you encounter issues:
1. Check this workflow guide
2. Review the script error messages
3. Verify file paths and permissions
4. Ensure all dependencies are installed

The workflow scripts provide detailed error messages to help diagnose issues.
