import os

def remove_collection_index_files(root_dir):
    """
    Recursively searches for and deletes all `collection_index.json` files
    in the specified `root_dir` and its subdirectories.

    Args:
    - root_dir (str): The root directory to start searching for `collection_index.json` files.
    """
    removed_files = 0  # Counter to track the number of files removed

    # Walk through all directories and subdirectories
    for current_root, dirs, files in os.walk(root_dir):
        # Check if "collection_index.json" exists in the current folder
        if "collection_index.json" in files:
            collection_index_path = os.path.join(current_root, "collection_index.json")
            try:
                os.remove(collection_index_path)
                print(f"Removed: {collection_index_path}")
                removed_files += 1
            except Exception as e:
                print(f"Failed to remove {collection_index_path}: {e}")

    print(f"Total `collection_index.json` files removed: {removed_files}")

def remove_main_index_files(root_dir):
    """
    Removes the main index.json files from the sample_packs and sccode_library directories
    that list all collections.

    Args:
    - root_dir (str): The root directory (project root)
    """
    # Define paths for the main directories
    sample_packs_dir = os.path.join(root_dir, "sample_packs")
    sccode_library_dir = os.path.join(root_dir, "sccode_library")
    
    removed_files = 0
    
    # Check and remove sample_packs/index.json
    sample_packs_index = os.path.join(sample_packs_dir, "index.json")
    if os.path.exists(sample_packs_index):
        try:
            os.remove(sample_packs_index)
            print(f"Removed: {sample_packs_index}")
            removed_files += 1
        except Exception as e:
            print(f"Failed to remove {sample_packs_index}: {e}")
    
    # Check and remove sccode_library/index.json
    sccode_library_index = os.path.join(sccode_library_dir, "index.json")
    if os.path.exists(sccode_library_index):
        try:
            os.remove(sccode_library_index)
            print(f"Removed: {sccode_library_index}")
            removed_files += 1
        except Exception as e:
            print(f"Failed to remove {sccode_library_index}: {e}")
    
    print(f"Total main index.json files removed: {removed_files}")

# Remove both collection_index.json files and main index.json files
remove_collection_index_files("..")
remove_main_index_files("..")