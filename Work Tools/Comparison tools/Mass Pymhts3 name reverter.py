import os

def rename_folders_with_xml_files(folder_path):
    # Get a list of all folders in the specified directory
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    # Iterate through each subfolder
    for subfolder in subfolders:
        try:
            # Get a list of all files in the subfolder
            files = os.listdir(subfolder)
            # Check if there is exactly one XML file in the subfolder
            xml_files = [file for file in files if file.endswith('.xml')]
            if len(xml_files) == 1:
                # Extract the name of the XML file without the extension
                xml_file_name = os.path.splitext(xml_files[0])[0]
                # Rename the subfolder to match the XML file name
                new_folder_name = os.path.join(folder_path, xml_file_name)
                os.rename(subfolder, new_folder_name)
                print(f"Renamed folder '{os.path.basename(subfolder)}' to '{xml_file_name}'")
            elif len(xml_files) > 1:
                print(f"Error: Multiple XML files found in '{os.path.basename(subfolder)}'. Skipping...")
            else:
                print(f"Error: No XML file found in '{os.path.basename(subfolder)}'. Skipping...")
        except Exception as e:
            print(f"An error occurred while processing folder '{os.path.basename(subfolder)}': {e}")
            continue

# Prompt the user to input the path to the folder
folder_path = input("Enter the path to the folder containing subfolders: ")

# Call the function to rename the folders
rename_folders_with_xml_files(folder_path)
