import os

def rename_csv_files():
    # Get the user prompted filepath
    filepath = input("Enter the directory path where CSV files are located: ")

    # Get the user prompted entry to prepend
    prepend_entry = input("Enter the text to prepend to the filenames: ")

    # List all files in the given directory
    files = os.listdir(filepath)

    # Iterate through the files and process CSV files
    for filename in files:
        if filename.endswith('.csv'):
            csv_path = os.path.join(filepath, filename)

            # Check if the specific CSV file exists and rename it if necessary
            if filename == 'aaSCD21-SDD21.csv':
                new_filename = f"{prepend_entry}_MCILR.csv"
            else:
                new_filename = f"{prepend_entry}_{filename}"

            # Full new path for renaming the file
            new_csv_path = os.path.join(filepath, new_filename)

            # Rename the file
            os.rename(csv_path, new_csv_path)

if __name__ == "__main__":
    rename_csv_files()
