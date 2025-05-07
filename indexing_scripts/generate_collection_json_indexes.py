import os
import shutil
import json
import requests
from urllib.parse import quote, urljoin
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def generate_file_tree_json(base_dir, base_url, output_json):
    """
    Generates a JSON file representing the file tree of `base_dir`.
    Each file entry in the tree contains a download link based on `base_url`.
    
    Args:
    - base_dir (str): The root directory to start scanning for files and folders.
    - base_url (str): The base URL used to create download links for each file.
    - output_json (str): Path to the output JSON file.
    """
    def build_tree(root):
        tree = {"name": os.path.basename(root), "path": root, "children": []}
        for entry in sorted(os.listdir(root)):
            full_path = os.path.join(root, entry)
            if os.path.isdir(full_path):
                tree["children"].append(build_tree(full_path))
            else:
                file_url = urljoin(base_url, quote(os.path.relpath(full_path, base_dir)))
                tree["children"].append({
                    "name": entry,
                    "path": full_path,
                    "url": file_url
                })
        return tree

    file_tree = build_tree(base_dir)
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(file_tree, json_file, indent=2)
    print(f"File tree JSON created at {output_json}")


def clean_directory(directory_path):
    """
    Recursively removes .DS_Store files, __pycache__ directories, and .pyc files
    from the specified directory.
    
    Args:
        directory_path (str): Path to the directory to clean
    
    Returns:
        dict: Counts of removed items by type
    """
    if not os.path.isdir(directory_path):
        raise ValueError(f"'{directory_path}' is not a valid directory")
    
    # Initialize counters
    removed = {
        "ds_store": 0,
        "pycache_dirs": 0,
        "pyc_files": 0
    }
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory_path, topdown=False):
        # Remove .DS_Store files
        for file in files:
            if file == ".DS_Store":
                file_path = os.path.join(root, file)
                os.remove(file_path)
                removed["ds_store"] += 1
                print(f"Removed: {file_path}")
            elif file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                removed["pyc_files"] += 1
                print(f"Removed: {file_path}")
        
        # Remove __pycache__ directories
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path)
                removed["pycache_dirs"] += 1
                print(f"Removed: {dir_path}")
    
    # Print summary
    print("\nCleanup Summary:")
    print(f"- Removed {removed['ds_store']} .DS_Store files")
    print(f"- Removed {removed['pycache_dirs']} __pycache__ directories")
    print(f"- Removed {removed['pyc_files']} .pyc files")
    
    return removed

def generate_folder_indexes(root_dir, base_url):
    """
    Traverses a directory tree starting at `root_dir` and, for each folder
    containing a `collection.json` file, generates a `collection_index.json` file
    with an adapted `base_url`.

    Args:
    - root_dir (str): The root directory to start searching for `collection.json` files.
    - base_url (str): The base URL to be used as the root when generating download links.
    """

    clean_directory(root_dir)

    for current_root, dirs, files in os.walk(root_dir):
        # Check if "collection.json" exists in the current folder
        if "collection.json" in files:
            # Define path for output index file
            collection_json_path = os.path.join(current_root, "collection.json")
            collection_index_path = os.path.join(current_root, "collection_index.json")

            # Calculate the relative path from root_dir to the current folder
            relative_path = os.path.relpath(current_root, root_dir)
            
            # Adjust the base URL for this folder by appending the relative path
            folder_base_url = urljoin(base_url, quote(relative_path) + '/')

            # Generate the index for this folder with the adjusted base URL
            generate_file_tree_json(current_root, folder_base_url, collection_index_path)
            print(f"Generated {collection_index_path} for folder containing collection.json with base URL {folder_base_url}")

def generate_main_indexes(root_dir, base_url):
    """
    Generates or updates the main index.json files in the sample_packs and sccode_library
    directories that list all collections in those directories.
    
    Args:
    - root_dir (str): The root directory (project root)
    - base_url (str): The base URL to be used as the root
    """
    # Define paths for the main directories
    sample_packs_dir = os.path.join(root_dir, "sample_packs")
    sccode_library_dir = os.path.join(root_dir, "sccode_library")
    
    # Process sample_packs directory
    if os.path.isdir(sample_packs_dir):
        collections = []
        
        # Iterate through subdirectories to find collections
        for item in sorted(os.listdir(sample_packs_dir)):
            item_path = os.path.join(sample_packs_dir, item)
            if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "collection.json")):
                collections.append({
                    "name": item,
                    "type": "samples"
                })
        
        # Create the index.json file
        index_path = os.path.join(sample_packs_dir, "index.json")
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump({"collections": collections}, f, indent=4)
        print(f"Generated {index_path} with {len(collections)} sample collections")
    
    # Process sccode_library directory
    if os.path.isdir(sccode_library_dir):
        collections = []
        
        # Iterate through subdirectories to find collections
        for item in sorted(os.listdir(sccode_library_dir)):
            item_path = os.path.join(sccode_library_dir, item)
            if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "collection.json")):
                collections.append({
                    "name": item,
                    "type": "sccode"
                })
        
        # Create the index.json file
        index_path = os.path.join(sccode_library_dir, "index.json")
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump({"collections": collections}, f, indent=4)
        print(f"Generated {index_path} with {len(collections)} sccode collections")

# Generate both collection_index.json files and main index.json files
generate_folder_indexes(".", "https://collections.renardo.org")
generate_main_indexes(".", "https://collections.renardo.org")