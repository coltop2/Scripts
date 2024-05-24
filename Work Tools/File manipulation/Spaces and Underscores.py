import os
import time


def replace_spaces_with_underscores(folder_path, replace_option):
    start_time = time.time()

    try:
        # Check if the provided path is a directory
        if not os.path.isdir(folder_path):
            print("Error: The provided path is not a directory.")
            return

        # Get a list of all files in the folder
        file_list = os.listdir(folder_path)

        # Iterate through each file
        for filename in file_list:
            if replace_option == 1 and "_" in filename:
                new_filename = filename.replace("_", " ")
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f"Replaced underscores with spaces: '{filename}' to '{new_filename}'")
            elif replace_option == 2 and " " in filename:
                new_filename = filename.replace(" ", "_")
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f"Replaced spaces with underscores: '{filename}' to '{new_filename}'")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Process completed in {elapsed_time:.4f} seconds.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")

    try:
        replace_option = int(input(
            "Select an option:\n1. Replace Underscores with Spaces\n2. Replace Spaces with Underscores\nEnter your choice (1 or 2): "))

        if replace_option not in [1, 2]:
            raise ValueError("Invalid option. Please enter 1 or 2.")

        replace_spaces_with_underscores(folder_path, replace_option)

    except ValueError as ve:
        print(f"Error: {ve}")
