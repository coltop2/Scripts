import os
import zipfile
from datetime import datetime


def delete_large_zip_files(data_path, max_size_mb, log_file_path):
    try:
        replaced_files = []
        for root, _, files in os.walk(data_path):
            for file in files:
                if file.endswith(".zip"):
                    zip_file_path = os.path.join(root, file)
                    zip_file_size_mb = os.path.getsize(zip_file_path) / (1024 * 1024)  # Size in MB
                    if zip_file_size_mb > max_size_mb:
                        # Delete the zip file
                        os.remove(zip_file_path)
                        replaced_files.append(zip_file_path)
                        # Create a txt file with the same name
                        txt_file_path = os.path.splitext(zip_file_path)[0] + ".txt"
                        with open(txt_file_path, "w") as txt_file:
                            txt_file.write("This file was created because the corresponding zip file was too large.")
                    print(f"Processed: {zip_file_path}")
        if replaced_files:
            # Generate log file name with current date/time
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_file_name = f"zip_replacement_{current_datetime}.txt"
            log_file_path = os.path.join(log_file_path, log_file_name)
            with open(log_file_path, "w") as log_file:
                log_file.write("\n".join(replaced_files))
            print(f"Log file created at: {log_file_path}")
        else:
            print("No oversized files found.")
            # Create an empty log file if no oversized files are found
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_file_name = f"zip_replacement_{current_datetime}.txt"
            log_file_path = os.path.join(log_file_path, log_file_name)
            with open(log_file_path, "w") as log_file:
                log_file.write("No oversized files found.")
            print(f"Empty log file created at: {log_file_path}")
        print("Operation completed.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        data_path = input("Enter the data path: ")
        if not os.path.isdir(data_path):
            print("Invalid data path.")
            exit()

        max_size_mb = float(input("Enter the maximum size in MB: "))
        if max_size_mb <= 0:
            print("Invalid maximum size.")
            exit()

        log_file_path = input("Enter the directory path to save the log file: ")
        if not os.path.isdir(log_file_path):
            print("Invalid log file directory path.")
            exit()

        delete_large_zip_files(data_path, max_size_mb, log_file_path)
    except ValueError:
        print("Invalid input for maximum size.")
