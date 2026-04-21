import os
import glob
import re

new_loader = """<div class="txt-loading">
                    <span data-text-preloader="R" class="letters-loading">
                        R
                    </span>
                    <span data-text-preloader="E" class="letters-loading">
                        E
                    </span>
                    <span data-text-preloader="T" class="letters-loading">
                        T
                    </span>
                    <span data-text-preloader="E" class="letters-loading">
                        E
                    </span>
                    <span data-text-preloader="C" class="letters-loading">
                        C
                    </span>
                    <span data-text-preloader="H" class="letters-loading">
                        H
                    </span>
                </div>"""

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = re.sub(r'<div class="txt-loading">.*?</div>', new_loader, content, flags=re.DOTALL)
    
    if modified != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(modified)
        print(f"Updated {f}")
