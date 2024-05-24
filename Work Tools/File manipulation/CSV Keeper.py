import os

def delete_non_csv_files(folder_path):
    try:
        # Walk through the folder and its subdirectories
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                # Delete files that are not .csv files
                if not filename.endswith('.csv'):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

        print("Deletion completed.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Get user input for the folder path
folder_path = input("Enter the folder path: ")

# Call the function to delete non-.csv files in the specified folder and its subdirectories
delete_non_csv_files(folder_path)
