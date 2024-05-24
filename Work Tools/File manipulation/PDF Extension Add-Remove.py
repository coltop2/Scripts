import os

folder_path = input("Enter the folder path: ")

# Check if the folder exists
if not os.path.exists(folder_path):
    print("Folder path does not exist.")
    exit()

action = input("Enter 'add' to add '.pdf' extension or 'remove' to remove '.pdf' extension: ")

# Get all files in the folder
files = os.listdir(folder_path)

# Iterate over the files
for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    # Check if it's a file and ends with ".pdf"
    if os.path.isfile(file_path):
        if action == "remove" and file_name.lower().endswith(".pdf"):
            new_file_name = file_name[:-4]  # Remove the last four characters (".pdf")
            new_file_path = os.path.join(folder_path, new_file_name)
        elif action == "add" and not file_name.lower().endswith(".pdf"):
            new_file_name = file_name + ".pdf"  # Add ".pdf" extension
            new_file_path = os.path.join(folder_path, new_file_name)
        else:
            continue

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_name} to {new_file_name}")
