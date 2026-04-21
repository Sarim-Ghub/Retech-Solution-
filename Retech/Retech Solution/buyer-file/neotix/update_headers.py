import os
import re

# Read index.html to extract the new header
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract from '<header id="header-sticky" class="header-1">' to '</header>'
header_match = re.search(r'<header id="header-sticky" class="header-1">.*?</header>', index_content, flags=re.DOTALL)

if not header_match:
    print("Could not find the header in index.html")
    exit(1)

new_header = header_match.group(0)

# Files to update based on user's request: About, Contact us, Blog
target_files = [
    'about.html',
    'contact.html',
    'news-details.html',
    'news.html',
    'news-grid.html'
]

for file_path in target_files:
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the old header with the new one
    # Note: different pages might have slightly different header class or id if they are variations.
    # But usually it's '<header id="header-sticky" class="header-1">' or similar.
    # We will look for <header id="header-sticky"...>...</header>
    
    modified_content = re.sub(
        r'<header id="header-sticky".*?</header>',
        new_header,
        content,
        flags=re.DOTALL
    )
    
    if modified_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        print(f"Updated header in {file_path}")
    else:
        print(f"No changes needed or header not found in {file_path}")
