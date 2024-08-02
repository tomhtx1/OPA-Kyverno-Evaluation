import os
import json

# Define the path to the cloned repository
repo_path = '/Users/oluwatomisin.omonira/Documents/bigbang'

# Function to recursively find all JSON files in a directory
def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

# Function to read and interpret JSON files
def read_and_interpret_json(json_files):
    for json_file in json_files:
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                interpret_json(data, json_file)
        except Exception as e:
            print(f"Error reading {json_file}: {e}")

# Function to interpret the content of a JSON file
def interpret_json(data, file_path):
    print(f"\nInterpreting file: {file_path}")
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict) and 'enabled' in value:
                status = "enabled" if value["enabled"] else "disabled"
                print(f"{key} is {status}")
            elif isinstance(value, dict) and 'git' in value:
                repo_info = value['git']
                print(f"{key}: repo={repo_info.get('repo', 'N/A')}, path={repo_info.get('path', 'N/A')}, branch={repo_info.get('branch', 'N/A')}")
            elif isinstance(value, dict):
                interpret_json(value, file_path)
            else:
                print(f"{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            interpret_json(item, file_path)
    else:
        print(data)

# Find all JSON files in the repository
json_files = find_json_files(repo_path)

# Read and interpret the JSON files
read_and_interpret_json(json_files)
