import os
import csv
from collections import defaultdict

def parse_and_separate(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            input_file = os.path.join(input_folder, filename)
            data_by_sn_pn = defaultdict(list)

            with open(input_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)  # Skip the header row
                for row in reader:
                    sn = row[13].split('-')[0]  # Extract the SN without suffix
                    pn = row[14]
                    key = f"{pn} {sn}"  # Switched the order of PN and SN
                    data_by_sn_pn[key].append(row)

            for key, data in data_by_sn_pn.items():
                output_file = os.path.join(output_folder, f"{key}.csv")
                with open(output_file, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(header)
                    writer.writerows(data)

if __name__ == "__main__":
    input_folder = input("Enter the path to the input folder containing CSV files: ")
    output_folder = input("Enter the path to the output folder for the new CSVs: ")

    if not os.path.exists(input_folder) or not os.path.exists(output_folder):
        print("Invalid input or output folder path. Please provide valid paths.")
    else:
        parse_and_separate(input_folder, output_folder)
        print("CSV files separated successfully.")
