import os
import shutil

#def find_char_and_get_next_two(s):
    #index = s.find('#')
    #if index != -1 and index + 2 < len(s):
        #return s[index + 1: index + 3]
    #else:
        #return None

def parse_network_path(path):
    # Normalize the path to handle any inconsistencies
    normalized_path = os.path.normpath(path)
    # Split the path into directories using the OS-specific separator
    directories = normalized_path.split(os.sep)
    return directories

def copy_case_file():
    # Step 1: Take user input for the network file path
    network_path = input("Enter the network file path: ")

#Ensure we handle the input path as a raw string to interpret backslashes correctly
    network_path = r"{}".format(network_path)

#Step 2: (Optional) Extract identifier after '#' if present
    identifier = find_char_and_get_next_two(network_path)
    if identifier:
        print(f"Identifier found: {identifier}")

#Step 3: Parse the network path into directories and subdirectories
    directories = parse_network_path(network_path)
    print("Directories and subdirectories:")
    for dir in directories:
        print(dir)

#Construct the source file path
    source_file = os.path.join(*directories)

#Step 4: Check if the source file exists
    if os.path.exists(source_file):
        # Define the destination path (modify as needed)
        destination = os.path.join("C:/destination_path", directories[-1])

#Step 5: Copy the file to the destination
        try:
            shutil.copy(source_file, destination)
            print(f"File copied to: {destination}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("The specified source file does not exist.")