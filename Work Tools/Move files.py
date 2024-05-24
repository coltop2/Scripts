import os
import shutil
import time

def copy_files(data_path, dest_path):
    # Get all files in the data path and its subdirectories
    file_list = []
    for root, dirs, files in os.walk(data_path):
        for file in files:
            file_list.append(os.path.join(root, file))

    total_files = len(file_list)
    copied_files = 0
    start_time = time.time()

    # Copy files to the destination path
    for file_path in file_list:
        shutil.copy(file_path, dest_path)
        copied_files += 1
        print(f"{copied_files}/{total_files} Copied")

    end_time = time.time()
    duration = end_time - start_time
    print(f"Files copied successfully! Total duration: {duration:.2f} seconds.")

# Prompt user for the data path
data_path = input("Enter the data path: ")

# Prompt user for the destination path
dest_path = input("Enter the destination path: ")

# Call the copy_files function
copy_files(data_path, dest_path)
