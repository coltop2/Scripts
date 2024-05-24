import os

def find_and_modify_s4p_files(folder_path, series_to_keep, series_to_delete):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.s4p'):
                file_path = os.path.join(root, file)
                if any(series in file for series in series_to_delete):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                elif not any(series in file for series in series_to_keep):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    series_to_keep = [
        "s4p_DUT",  # <-- Modify this to the first series of characters to keep
        "2024",  # <-- Modify this to the second series of characters to keep
        "series3"   # <-- Modify this to the third series of characters to keep
    ]
    series_to_delete = [
        "left_DUT",  # <-- Modify this to the first series of characters to delete
        "orig_DUT",  # <-- Modify this to the second series of characters to delete
        "right_DUT"   # <-- Modify this to the third series of characters to delete
    ]
    find_and_modify_s4p_files(folder_path, series_to_keep, series_to_delete)
