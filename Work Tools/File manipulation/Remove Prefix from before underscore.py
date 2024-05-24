import os
import time


def rename_csv_files(path):
    mcilr_found = False
    renamed_files = []

    start_time = time.time()

    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            new_filename = filename.split("_", 1)[-1]
            new_path = os.path.join(path, new_filename)
            os.rename(os.path.join(path, filename), new_path)
            renamed_files.append(new_filename)
            print(f"Renamed {filename} to {new_filename}")

            if new_filename == "MCILR.csv":
                mcilr_found = True

    if mcilr_found:
        new_mcilr_filename = "SCD21-SDD21.csv"
        new_mcilr_path = os.path.join(path, new_mcilr_filename)
        os.rename(os.path.join(path, "MCILR.csv"), new_mcilr_path)
        renamed_files.append(new_mcilr_filename)
        print(f"Renamed MCILR.csv to {new_mcilr_filename}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Renaming completed. Time taken: {elapsed_time:.2f} seconds.")

    return renamed_files


# Usage example
user_provided_path = input("Enter the path to the directory containing CSV files: ")
renamed_files = rename_csv_files(user_provided_path)
