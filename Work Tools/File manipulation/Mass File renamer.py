import os

def rename_files(path, operation, modification, value, include_subdirectories=True, include_folders=True):
    try:
        if include_subdirectories:
            file_iterator = os.walk(path)
        else:
            file_iterator = [(path, [], os.listdir(path))]

        for root, dirs, files in file_iterator:
            for filename in files + (dirs if include_folders else []):
                old_path = os.path.join(root, filename)

                if os.path.isfile(old_path) or (os.path.isdir(old_path) and include_folders):
                    new_filename = modify_text(filename, operation, modification, value)
                    new_path = os.path.join(root if root else "", new_filename)

                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

        print("Renaming complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

def modify_text(text, operation, modification, value):
    if operation == "add":
        if modification == "prefix":
            return f"{value}{text}"
        elif modification == "suffix":
            return f"{text}{value}"
    elif operation == "remove":
        if modification == "front":
            return text[len(value):] if text.startswith(value) else text
        elif modification == "back":
            return text[:-len(value)] if text.endswith(value) else text

def main():
    path = input("Enter the file path: ")
    include_subdirectories = input("Include subdirectories? (yes/no): ").lower() == 'yes'
    include_folders = input("Include folders in the process? (yes/no): ").lower() == 'yes'

    operation = input("Choose operation (add/remove): ")
    if operation not in ["add", "remove"]:
        print("Invalid operation. Please choose 'add' or 'remove'.")
        return

    modification = input("Enter modification type (prefix/suffix/front/back): ")
    if modification not in ["prefix", "suffix", "front", "back"]:
        print("Invalid modification type. Please choose 'prefix', 'suffix', 'front', or 'back'.")
        return

    value = input("Enter text to add or number of characters to remove: ")

    rename_files(path, operation, modification, value, include_subdirectories, include_folders)

if __name__ == "__main__":
    main()
