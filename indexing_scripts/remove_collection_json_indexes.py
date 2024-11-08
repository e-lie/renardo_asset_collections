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

# Example usage:
# This will search through the `./docs` directory and delete all `collection_index.json` files it finds.
remove_collection_index_files(".")
