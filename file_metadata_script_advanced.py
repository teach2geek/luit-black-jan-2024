import os

def get_files_info_recursive(path='.'):
    # Initialize a list to store file information
    files_info = []

    # Check if the given path is a valid directory
    if not os.path.isdir(path):
        print(f"The path {path} is not a valid directory.")
        return files_info

    # Recursively walk through the directory
    for root, dirs, files in os.walk(path):
        # Iterate over each file in the directories
        for name in files:
            # Join the directory path and file name
            filepath = os.path.join(root, name)
            # Create a dictionary with file path and size
            file_info = {'name': filepath, 'size': os.path.getsize(filepath)}
            # Append the file info to the list
            files_info.append(file_info)

    return files_info

# Input the path or use the current directory as default
input_path = input("Enter the directory path (leave blank for current directory): ").strip()
input_path = input_path or '.'

# Execute the function and print the results
file_list = get_files_info_recursive(input_path)
for file in file_list:
    print(file)