import os


def rename_files(folder_path):
    # List all files and directories in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".s4p_DUT.s4p"):
                # Construct the new file name
                new_file_name = file_name.replace(".s4p_DUT", "")

                # Construct full paths for the old and new file names
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_file_name)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {old_file_path} to {new_file_path}")


# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")

# Call the function to rename files in the specified folder and its subdirectories
rename_files(folder_path)
