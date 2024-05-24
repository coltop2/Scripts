import os
import csv
import time


def delete_entries_below_row(file_path, row_number):
    with open(file_path, 'r') as file:
        rows = list(csv.reader(file))

    if row_number >= len(rows):
        print("Invalid row number.")
        return

    # Keep the rows up to the specified row number
    rows = rows[:row_number + 1]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Deleted entries below row {row_number} in {file_path}")


def process_csv_files(folder_path, row_number):
    start_time = time.time()
    total_files_processed = 0

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.csv') and file_name not in ['ZDD11.csv', 'ZDD22.csv']:
                file_path = os.path.join(root, file_name)
                delete_entries_below_row(file_path, row_number)
                total_files_processed += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nProcessed {total_files_processed} CSV files in {elapsed_time:.2f} seconds.")


def main():
    folder_path = input("Enter the folder path: ")
    row_number = int(input("Enter the row number (0-indexed) to delete entries below: "))

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    process_csv_files(folder_path, row_number)


if __name__ == '__main__':
    main()
