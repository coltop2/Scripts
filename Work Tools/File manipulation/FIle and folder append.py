import os

def list_files_and_folders(folder_path):
    # List all files and folders in the specified folder
    items = os.listdir(folder_path)
    return items

def rename_items(folder_path, text_to_add, position):
    items = list_files_and_folders(folder_path)

    for item in items:
        old_path = os.path.join(folder_path, item)

        # Determine new name based on user preferences
        if position.lower() == "front":
            new_name = f"{text_to_add}_{item}"
        elif position.lower() == "back":
            name_parts = os.path.splitext(item)
            new_name = f"{name_parts[0]}_{text_to_add}{name_parts[1]}"
        else:
            print("Invalid position. Please choose 'front' or 'back'.")
            return

        new_path = os.path.join(folder_path, new_name)

        # Rename the file/folder
        os.rename(old_path, new_path)

if __name__ == "__main__":
    # Prompt user for folder path
    folder_path = input("Enter the folder path: ")

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder not found.")
    else:
        # List files and folders
        items = list_files_and_folders(folder_path)
        print("Items in the folder:")
        for item in items:
            print(f"- {item}")

        # Prompt user for text to add and position
        text_to_add = input("Enter the text to add: ")
        position = input("Enter the position (front/back): ")

        # Rename items in the folder
        rename_items(folder_path, text_to_add, position)

        print("Items renamed successfully.")
