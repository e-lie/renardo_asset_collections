import os
import shutil


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



clean_directory(".")