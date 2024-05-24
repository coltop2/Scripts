import os
import time


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def contains_zdd11_or_zdd22(file_name):
    return "ZDD11" in file_name.upper() or "ZDD22" in file_name.upper()


def process_csv_files(folder_path, divisor, include_subfolders=False):
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith('.csv') and not contains_zdd11_or_zdd22(filename):
                file_path = os.path.join(root, filename)
                start_time = time.time()
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                with open(file_path, 'w') as file:
                    for line in lines:
                        entries = line.strip().split(',')
                        if entries:
                            first_entry = entries[0].strip()
                            if is_number(first_entry):
                                new_value = float(first_entry) / divisor
                                entries[0] = str(new_value)
                        new_line = ','.join(entries) + '\n'
                        file.write(new_line)

                end_time = time.time()
                processing_time = end_time - start_time
                print(f"File '{filename}' processed in {processing_time:.4f} seconds.")


if __name__ == "__main__":
    folder_path = input("Enter the folder path where CSV files are located: ")
    divisor = float(input("Enter the number you want to divide by: "))

    include_subfolders_input = input("Do you want to process CSV files in subfolders? (yes/no): ").lower().strip()
    include_subfolders = include_subfolders_input == "yes"

    process_csv_files(folder_path, divisor, include_subfolders)
    print("CSV files processed successfully.")
