import pathlib

def normalise_filename(directory):
    """
    Recursively traverses a directory and renames files by removing '#' characters.
    
    Args:
        directory (str): Path to the root directory containing files to rename
    """
    # Convert to Path object
    dir_path = pathlib.Path(directory)
    
    # Recursively iterate through all files
    for filepath in dir_path.rglob('*'):
        # Skip directories
        if filepath.is_dir():
            continue
        
        # Remove '#' from filename
        new_filename = filepath.name.replace('#', '_sharp_')
        
        # Create new filepath
        new_filepath = filepath.with_name(new_filename)
        
        # Rename if the filename has changed
        if new_filename != filepath.name:
            try:
                filepath.rename(new_filepath)
                print(f"Renamed: {filepath.name} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {filepath.name}: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the path to your directory
    target_directory = "/path/to/your/directory"
    normalise_filename(target_directory)