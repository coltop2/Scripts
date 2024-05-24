import os
import time
from datetime import datetime


def rename_folders(data_path):
    start_time = time.time()  # Start the timer
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Get current timestamp

    for root, dirs, files in os.walk(data_path):
        for directory in dirs:
            current_dir = os.path.join(root, directory)
            parent_folder = os.path.basename(root)
            for subdir in os.listdir(current_dir):
                subdir_path = os.path.join(current_dir, subdir)
                new_name = os.path.join(current_dir, f" {directory} {subdir}")
                os.rename(subdir_path, new_name)

    end_time = time.time()  # Stop the timer
    elapsed_time = end_time - start_time
    print(f"Renaming process completed in {elapsed_time:.2f} seconds.")


# Prompt the user for the data path
data_path = input("Enter the data path: ")

# Call the function to rename the folders
rename_folders(data_path)
