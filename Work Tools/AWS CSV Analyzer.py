import os
import csv

def check_csv_file(csv_file, limit):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        # Find the column indices for BER values
        ber_indices = [header.index(f'BER[{i}]') for i in range(8)]

        failed_lines = []

        # Iterate through the CSV data and check BER values
        for line_num, row in enumerate(reader, start=1):
            time = row[header.index('PassedTime')]
            for ber_index in ber_indices:
                ber_value = float(row[ber_index])
                if ber_value > limit:
                    failed_lines.append((csv_file, line_num, time, ber_index, ber_value))

        return failed_lines

def process_folder(folder_path, limit):
    failed_lines_all = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            csv_file = os.path.join(folder_path, filename)
            failed_lines = check_csv_file(csv_file, limit)
            failed_lines_all.extend(failed_lines)

    return failed_lines_all

# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")

# Prompt the user for the limit in scientific notation
limit = float(input("Enter the limit in scientific notation (e.g., 1.00e-12): "))

failed_lines_all = process_folder(folder_path, limit)

# Display results in the dialogue box
if failed_lines_all:
    message = "Failures found:\n"
    for csv_file, line_num, time, ber_index, ber_value in failed_lines_all:
        message += f"File: {csv_file}, Line {line_num}, Time: {time}, BER[{ber_index}] = {ber_value}\n"
    print(message)
else:
    print("No failures found.")
