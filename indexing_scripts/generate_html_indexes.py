import os
import sys
import fnmatch
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape
from urllib.parse import urljoin, quote

# Configure Jinja environment
env = Environment(loader=FileSystemLoader(searchpath=''), autoescape=select_autoescape(['html']))

# Jinja HTML template for folder index
template_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index of {{ current_dir }}</title>
</head>
<body>
    <h1>Index of {{ current_dir }}</h1>
    <ul>
        {% if parent_dir %}
            <li><a href="{{ parent_dir }}">.. (Parent Directory)</a></li>
        {% endif %}
        {% for folder in folders %}
            <li><a href="{{ base_url }}{{current_dir}}/{{ folder }}">{{ folder }}/</a></li>
        {% endfor %}
        {% for file in files %}
            <li><a href="{{ base_url }}{{current_dir}}/{{ file }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# Compile the template
template = env.from_string(template_content)

def load_gitignore_patterns(gitignore_path):
    """Load patterns from .gitignore file"""
    patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    patterns.append(line)
    return patterns

def should_ignore_file(file_path, gitignore_patterns, specific_ignore_files):
    """Check if a file should be ignored based on .gitignore patterns and specific files"""
    # Check if the file is in the list of specific files to ignore
    filename = os.path.basename(file_path)
    if filename in specific_ignore_files:
        return True
    
    # Check if the file matches any gitignore pattern
    for pattern in gitignore_patterns:
        # Convert gitignore pattern to fnmatch pattern
        if pattern.startswith('**/'):
            pattern = pattern[3:]
        if '*' in pattern or '?' in pattern or '[' in pattern:
            if fnmatch.fnmatch(file_path, pattern) or fnmatch.fnmatch(filename, pattern):
                return True
    
    return False

def should_ignore_directory(dir_path, gitignore_patterns, specific_ignore_dirs):
    """Check if a directory should be ignored based on .gitignore patterns and specific directories"""
    # Check if the directory is in the list of specific directories to ignore
    dirname = os.path.basename(dir_path)
    if dirname in specific_ignore_dirs:
        return True
    
    # Check if the directory matches any gitignore pattern
    for pattern in gitignore_patterns:
        # Look for directory patterns that end with /
        if pattern.endswith('/'):
            pattern = pattern[:-1]
        if pattern.startswith('**/'):
            pattern = pattern[3:]
        if fnmatch.fnmatch(dirname, pattern):
            return True
    
    return False

def generate_index_html(base_dir, base_url):
    # Load .gitignore patterns
    gitignore_path = os.path.join(base_dir, '.gitignore')
    gitignore_patterns = load_gitignore_patterns(gitignore_path)
    
    # Specific files and directories to ignore
    specific_ignore_files = ['.gitignore', 'uv.lock', '.python-version', 'pyproject.toml']
    specific_ignore_dirs = ['indexing_scripts', '__pycache__', '.git', '.claude', '.vscode', '.venv']
    
    for root, dirs, files in os.walk(base_dir):
        # Determine the folder name (we use index.html for each folder)
        folder_name = os.path.basename(root) or "root"  # "root" for base directory
        index_filename = "index.html"  # Always name the file index.html
        index_file_path = os.path.join(root, index_filename)

        # Get the relative path of the current directory from base_dir
        current_dir = os.path.relpath(root, base_dir)

        # Calculate the parent directory link (point to its prefixed index.html)
        if current_dir == ".":
            parent_dir = None  # No parent link for the base directory
        else:
            parent_folder_name = os.path.basename(os.path.dirname(root)) or "root"
            parent_dir = os.path.join(base_url, os.path.relpath(os.path.join(root, ".."), base_dir))

        # Filter out directories to be ignored
        dirs[:] = [d for d in dirs if not should_ignore_directory(os.path.join(root, d), gitignore_patterns, specific_ignore_dirs)]
        
        # Filter out files to be ignored
        filtered_files = []
        for file in files:
            if file != index_filename and not should_ignore_file(os.path.join(root, file), gitignore_patterns, specific_ignore_files):
                filtered_files.append(file)

        # URL encode folder and file names
        encoded_dirs = [quote(d) for d in sorted(dirs)]
        encoded_files = [quote(f) for f in sorted(filtered_files)]

        # Render the HTML content
        html_content = template.render(
            current_dir=current_dir,
            parent_dir=parent_dir,
            folders=encoded_dirs,
            files=encoded_files,
            base_url=base_url
        )

        # Write the HTML file
        with open(index_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Generated {index_file_path}")


base_directory = "."
base_url = 'https://collections.renardo.org/' 

generate_index_html(base_directory, base_url)
