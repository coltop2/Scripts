import os
import time

def delete_lines_below(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            file.writelines(lines[:line_number])
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def process_files(folder_path, extension, line_number):
    start_time = time.time()

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(extension):
                file_path = os.path.join(root, file_name)
                print(f"Processing file: {file_path}")
                delete_lines_below(file_path, line_number)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Processing complete. Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    extension = ".s4p"

    if os.path.exists(folder_path):
        try:
            line_number = int(input("Enter the line number to keep (delete everything below): "))
            process_files(folder_path, extension, line_number)
        except ValueError:
            print("Invalid input. Please enter a valid line number.")
    else:
        print("Invalid folder path. Please provide a valid path.")
