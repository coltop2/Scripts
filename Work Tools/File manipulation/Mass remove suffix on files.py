import os

def rename_files_in_directory(directory, include_subfolders=False, num_chars=None):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                old_path = os.path.join(root, file)
                new_name = file[:num_chars] + ".zip"
                new_path = os.path.join(root, new_name)
                try:
                    os.rename(old_path, new_path)
                    print("Renamed '{}' to '{}'.".format(old_path, new_path))
                except Exception as e:
                    print("Error renaming '{}': {}".format(old_path, e))

def main():
    directory = input("Enter the path of the directory: ")
    include_subfolders = input("Include subfolders? (y/n): ").lower() == 'y'
    num_chars = input("Enter the number of characters to keep for all zip files (e.g., 5): ")
    try:
        num_chars = int(num_chars)
    except ValueError:
        print("Please enter a valid number.")
        return
    rename_files_in_directory(directory, include_subfolders, num_chars)

if __name__ == "__main__":
    main()
