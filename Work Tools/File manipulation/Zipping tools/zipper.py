import os
import zipfile
import time

def zip_files_in_folders(folder_path, destination_folder):
    start_time = time.time()

    for root, dirs, files in os.walk(folder_path):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            folder_name = os.path.basename(folder_path)
            zip_filename = f"{folder_name}.zip"
            zip_path = os.path.join(root, zip_filename)

            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    zipf.write(file_path, file)

            destination_path = os.path.join(destination_folder, zip_filename)
            os.rename(zip_path, destination_path)
            print(f"Folder '{folder_name}' has been zipped and saved to '{destination_path}'.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds.")

user_prompted_folder = input("Enter the folder path to folders: ")
destination_folder = input("Enter the destination folder path: ")
zip_files_in_folders(user_prompted_folder, destination_folder)
