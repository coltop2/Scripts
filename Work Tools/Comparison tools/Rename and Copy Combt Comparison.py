import os
import shutil
import time


def rename_files(directory_path):
    parent_folder_name = os.path.basename(directory_path)
    file_list = os.listdir(directory_path)

    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)

        if os.path.isdir(file_path):
            subfolder_name = file_name
            subfolder_path = os.path.join(directory_path, subfolder_name)
            rename_files(subfolder_path)  # Recursive call for subfolders
        else:
            new_name = f"{parent_folder_name} {file_name}"
            old_path = os.path.join(directory_path, file_name)
            new_path = os.path.join(directory_path, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed {file_name} to {new_name}")

    print(f"File renaming complete for folder: {parent_folder_name}")


def count_files(source_path):
    file_count = 0
    for root, _, files in os.walk(source_path):
        file_count += len(files)
    return file_count


def copy_files_to_destination(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    total_files = count_files(source_path)
    file_count = 0

    for root, _, files in os.walk(source_path):
        if len(files) > 0:
            for filename in files:
                source_file = os.path.join(root, filename)
                destination_file = os.path.join(destination_path, filename)

                # Check if the file already exists in the destination path
                if os.path.exists(destination_file):
                    print(f"Skipping duplicate file: {filename}")
                    continue

                shutil.copy2(source_file, destination_file)
                file_count += 1
                print(f"{file_count}/{total_files} Copied")


def main():
    input_path = input("Enter the folder path: ")
    consolidated_path = os.path.join(input_path, "Consolidated")

    start_time = time.time()

    rename_files(input_path)
    copy_files_to_destination(input_path, consolidated_path)

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Process completed in {total_time:.2f} seconds.")


if __name__ == "__main__":
    main()
