from pathlib import Path
import shutil
import string
import sys

def reorganize_folders(input_path: Path, output_path: Path):
    """
    Reorganize folder structure from:
        input/
            a/
                upper/
                lower/
            b/
                upper/
                lower/
            ...
    to:
        output/
            a/
            b/
            ...
            A/
            B/
            ...
    """
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Process each lowercase letter
    for letter in string.ascii_lowercase:
        src_folder = input_path / letter
        
        # Skip if source letter folder doesn't exist
        if not src_folder.exists():
            print(f"Warning: Source folder '{letter}' not found, skipping...")
            continue
            
        # Create lowercase destination folder
        lower_dest = output_path / letter
        lower_dest.mkdir(exist_ok=True)
        
        # Create uppercase destination folder
        upper_dest = output_path / letter.upper()
        upper_dest.mkdir(exist_ok=True)
        
        # Process lower subfolder
        lower_src = src_folder / "lower"
        if lower_src.exists():
            # Copy all files from lower to lowercase destination
            for file in lower_src.glob("*"):
                if file.is_file():
                    shutil.copy2(file, lower_dest / file.name)
        else:
            print(f"Warning: 'lower' subfolder not found in '{letter}' folder")
            
        # Process upper subfolder
        upper_src = src_folder / "upper"
        if upper_src.exists():
            # Copy all files from upper to uppercase destination
            for file in upper_src.glob("*"):
                if file.is_file():
                    shutil.copy2(file, upper_dest / file.name)
        else:
            print(f"Warning: 'upper' subfolder not found in '{letter}' folder")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)
        
    input_path = Path(sys.argv[1]).resolve()
    output_path = Path(sys.argv[2]).resolve()
    
    # Validate input path
    if not input_path.exists():
        print(f"Error: Input folder '{input_path}' does not exist")
        sys.exit(1)
        
    # Validate input is not the same as output
    if input_path == output_path:
        print("Error: Input and output folders cannot be the same")
        sys.exit(1)
        
    # Validate output parent exists
    if not output_path.parent.exists():
        print(f"Error: Output parent folder '{output_path.parent}' does not exist")
        sys.exit(1)
    
    try:
        print(f"Reorganizing folders from '{input_path}' to '{output_path}'...")
        reorganize_folders(input_path, output_path)
        print("Done!")
    except Exception as e:
        print(f"Error during folder reorganization: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
