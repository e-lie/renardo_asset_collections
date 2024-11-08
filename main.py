from indexing_scripts.generate_html_indexes import generate_index_html
from indexing_scripts.remove_html_indexes import remove_html_files
from indexing_scripts.generate_collection_json_indexes import generate_folder_indexes
from indexing_scripts.remove_collection_json_indexes import remove_collection_index_files


base_directory = "."
base_url = 'http://collections.renardo.org/' 

remove_collection_index_files(base_directory)
remove_html_files(base_directory)
generate_folder_indexes(base_directory, base_url)
generate_index_html(base_directory, base_url)