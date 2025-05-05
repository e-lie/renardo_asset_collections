import os
import json
import requests


def download_json_from_url(url):
    """
    Download JSON content from a given HTTP URL.
    
    Args:
    - url (str): The URL to fetch the JSON from.
    
    Returns:
    - dict: Parsed JSON content.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status
    return response.json()



def download_files_from_json(json_url, download_dir):
    """
    Parses a JSON file containing a file tree with download links,
    and downloads each file to `download_dir`.
    
    Args:
    - json_file (str): Path to the JSON file with file structure and download links.
    - download_dir (str): Local directory where files will be downloaded.
    """

    def download_file(url, destination, retries=5):
        attempt = 1
        while attempt <= retries:
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                with open(destination, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Downloaded {destination}")
                return  # Successful download, exit the function
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt} failed for {url}: {e}")
                attempt += 1
                if attempt <= retries:
                    time.sleep(2)  # Wait before retrying
        print(f"Failed to download {url} after {retries} attempts")

    def process_node(node, base_path):
        if "url" in node:
            # This is a file node; download it
            file_path = os.path.join(base_path, node["name"])
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            download_file(node["url"], file_path)
        elif "children" in node:
            # This is a folder node; process its children
            folder_path = os.path.join(base_path, node["name"])
            os.makedirs(folder_path, exist_ok=True)
            for child in node["children"]:
                process_node(child, folder_path)

    # Load the JSON structure
    # with open(json_file, "r", encoding="utf-8") as f:
        # file_tree = json.load(f)

    # Download JSON content from URL
    file_tree = download_json_from_url(json_url)

    # Start processing the tree
    process_node(file_tree, download_dir)
    print(f"All files downloaded to {download_dir}")

download_files_from_json("http://localhost:8000/samples/0_foxdot_default/collection_index.json", "./downloaded_files")
