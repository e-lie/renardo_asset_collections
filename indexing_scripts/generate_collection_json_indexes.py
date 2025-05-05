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

# def generate_folder_indexes(root_dir, base_url):
#     """
#     Traverses a directory tree starting at `root_dir` and, for each folder
#     containing a `collection.json` file, generates a `collection_index.json` file.

#     Args:
#     - root_dir (str): The root directory to start searching for `collection.json` files.
#     - base_url (str): The base URL to be used when generating download links.
#     """
#     for current_root, dirs, files in os.walk(root_dir):
#         # Check if "collection.json" exists in the current folder
#         if "collection.json" in files:
#             # Define path for output index file
#             collection_json_path = os.path.join(current_root, "collection.json")
#             collection_index_path = os.path.join(current_root, "collection_index.json")

#             # Generate the index for this folder
#             generate_file_tree_json(current_root, base_url, collection_index_path)
#             print(f"Generated {collection_index_path} for folder containing collection.json")


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


# generate_file_tree_json("./samples", "http://localhost:8000/", "file_tree.json")

generate_folder_indexes(".", "https://collections.renardo.org")
