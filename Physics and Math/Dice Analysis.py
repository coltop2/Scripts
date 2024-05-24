import os
import csv
from collections import Counter
import datetime


# Function to list and select a CSV file from the provided directory
def select_csv_file(directory):
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    if not csv_files:
        print("No CSV files found in the directory.")
        return None

    print("List of CSV files:")
    for i, file_name in enumerate(csv_files, start=1):
        print(f"{i}. {file_name}")

    while True:
        try:
            selection = int(input("Enter the number of the CSV file you want to process: "))
            if 1 <= selection <= len(csv_files):
                return csv_files[selection - 1]
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to analyze the last column of a CSV file and create a summary CSV
def analyze_csv_last_column(file_path, output_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row:
                last_column = row[-1]
                try:
                    value = int(last_column)
                    data.append(value)
                except ValueError:
                    print(f"Skipping invalid value in row: {last_column}")

    if data:
        counter = Counter(data)
        total_entries = len(data)
        output_csv_file = os.path.join(output_path, f"{datetime.datetime.now():%m.%d.%Y.%H.%M.%S}.csv")

        with open(output_csv_file, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Value", "Entries", "Percentage"])
            for key, value in counter.items():
                percentage = (value / total_entries) * 100
                writer.writerow([key, value, f"{percentage:.2f}%"])

        print(f"Analysis summary has been saved to {output_csv_file}")
    else:
        print("No valid data found in the last column.")


if __name__ == "__main__":
    directory = input("Enter the directory path where CSV files are located: ")

    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Invalid directory path.")
    else:
        selected_file = select_csv_file(directory)
        if selected_file:
            file_path = os.path.join(directory, selected_file)
            output_path = input("Enter the directory path to save the output CSV: ")
            analyze_csv_last_column(file_path, output_path)
