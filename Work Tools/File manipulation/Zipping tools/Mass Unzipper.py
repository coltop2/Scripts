import os
import zipfile
import shutil

def unzip_all(folder):
    # Iterate through all files and directories in the given folder
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                # Extract folder name from the zip file name
                folder_name = os.path.splitext(file)[0]
                # Create a directory with the same name as the zip file
                extract_path = os.path.join(root, folder_name)
                os.makedirs(extract_path, exist_ok=True)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # Extract all contents of the zip file to the newly created directory
                    zip_ref.extractall(extract_path)
                # Remove the original zip file
                os.remove(zip_path)
                print(f"Finished extracting {zip_path}")

# Prompt the user to provide the folder path
folder_path = input("Please provide the folder path: ")

# Check if the provided path exists
if not os.path.exists(folder_path):
    print("The provided folder path does not exist.")
else:
    # Call the function to unzip all zip files in the folder and its subfolders
    unzip_all(folder_path)
