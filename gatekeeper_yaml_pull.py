import os
import yaml
import glob

def pull_and_organize_yaml_files(repo_path, output_file):
    # Check if the provided path is a valid directory
    if not os.path.isdir(repo_path):
        print(f"The path '{repo_path}' is not a valid directory.")
        return

    # Find all YAML files in the repository
    yaml_files = glob.glob(os.path.join(repo_path, '**', '*.yaml'), recursive=True) + \
                 glob.glob(os.path.join(repo_path, '**', '*.yml'), recursive=True)
    
    # Check if any YAML files were found
    if not yaml_files:
        print(f"No YAML files found in the directory '{repo_path}'.")
        return
    
    print(f"Found {len(yaml_files)} YAML files.")

    # Create a dictionary to store the contents of the YAML files
    yaml_data = {}
    
    for file in yaml_files:
        print(f"Processing file: {file}")
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data is None:
                    print(f"Warning: {file} is empty or could not be parsed.")
                    continue
                file_name = os.path.relpath(file, repo_path)
                if file_name not in yaml_data:
                    yaml_data[file_name] = data
                else:
                    print(f"Duplicate found for file: {file_name}. Skipping.")
                print(f"Successfully read: {file_name}")
        except yaml.YAMLError as e:
            print(f"Skipping invalid YAML file: {file} - Error: {e}")
        except Exception as e:
            print(f"Unexpected error reading file {file}: {e}")
    
    if not yaml_data:
        print("No valid YAML data found.")
        return
    
    # Sort the dictionary by the file names (keys)
    sorted_yaml_data = dict(sorted(yaml_data.items()))
    
    # Save the organized data into a Markdown file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for file_name, data in sorted_yaml_data.items():
                f.write(f"## {file_name}\n")
                f.write("```yaml\n")
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)
                f.write("```\n\n")
        print(f"Organized data has been saved to {output_file}")
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}")

# Specify the path to the cloned repository and the output file
repo_path = '/Users/oluwatomisin.omonira/Gatekeeper'  # Replace with the actual path
output_file = 'organized_yaml_files.md'

# Run the function to pull and organize YAML files
pull_and_organize_yaml_files(repo_path, output_file)
