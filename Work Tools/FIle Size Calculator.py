import os
import time


def get_folder_size(folder_path):
    total_size = 0
    processed_files = 0

    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
            processed_files += 1
            if processed_files % 10 == 0:
                print(f"Processed {processed_files} files")

    return total_size


# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")

# Validate if the folder path is valid
if not os.path.isdir(folder_path):
    print("Invalid folder path")
else:
    # Calculate the size
    start_time = time.time()
    size_in_bytes = get_folder_size(folder_path)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convert to appropriate units
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    size_in_gb = size_in_mb / 1024

    print(f"\nSize of '{folder_path}':")
    print(f"Bytes: {size_in_bytes}")
    print(f"KB: {size_in_kb}")
    print(f"MB: {size_in_mb}")
    print(f"GB: {size_in_gb}")
    print(f"\nElapsed time: {elapsed_time:.2f} seconds")
