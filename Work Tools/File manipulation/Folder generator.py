import os


def create_folders_from_file(file_path, base_folder):
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found.")
        return

    # Create the base folder if it doesn't exist
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    # Open the file and read its lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Remove leading and trailing whitespace and invalid characters for folder names
            folder_name = line.strip().replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace(
                '?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
            folder_path = os.path.join(base_folder, folder_name)

            # Create the folder
            try:
                os.makedirs(folder_path)
                print(f"Created folder: {folder_name}")
            except FileExistsError:
                print(f"Folder '{folder_name}' already exists.")


if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    base_folder = input("Enter the path where you want to create folders: ")
    create_folders_from_file(file_path, base_folder)
