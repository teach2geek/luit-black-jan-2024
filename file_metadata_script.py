import os

def get_files_info():
    # Initialize a list to hold file information
    files_info = []

    # Loop through each file in the current directory
    for filename in os.listdir('.'):
        # Check if the entry is a file
        if os.path.isfile(filename):
            # Create a dictionary with file name and size
            file_info = {'name': filename, 'size': os.path.getsize(filename)}
            # Append the file info to the list
            files_info.append(file_info)

    return files_info

# Execute the function and print the results
file_list = get_files_info()
print(file_list)