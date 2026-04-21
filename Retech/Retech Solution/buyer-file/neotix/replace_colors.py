import os
import glob
import re

# Files to scan
css_files = glob.glob('assets/css/**/*.css', recursive=True)
scss_files = glob.glob('assets/scss/**/*.scss', recursive=True)
all_files = css_files + scss_files

for f in all_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {f}: {e}")
        continue
    
    # Replacements
    # 1. Hex codes
    new_content = re.sub(r'#f94d00', '#00b4d8', content, flags=re.IGNORECASE)
    
    # 2. RGB values inside rgba
    # We want to match exactly `249, 77, 0` or variations of spaces
    new_content = re.sub(r'249,\s*77,\s*0', '0, 180, 216', new_content)
    
    if new_content != content:
        try:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated colors in: {f}")
        except Exception as e:
            print(f"Error writing {f}: {e}")
