import os

def list_files_and_folders(input_folder):
    with open('file_list.txt', 'w') as file:
        for root, dirs, files in os.walk(input_folder):
            file.write(f'Folder: {root}\n')
            for f in files:
                file_path = os.path.join(root, f)
                file_extension = os.path.splitext(f)[1]
                file.write(f'  File: {f} ({file_extension})\n')

if __name__ == "__main__":
    # Prompt user for input folder
    input_folder = input("Enter the path of the folder: ")

    # Verify if the folder exists
    if not os.path.exists(input_folder):
        print("The specified folder does not exist.")
    else:
        # Prompt user for output folder
        output_folder = input("Enter the path of the output folder: ")

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Generate the list of files and folders
        list_files_and_folders(input_folder)

        # Move the generated file to the output folder
        output_file_path = os.path.join(output_folder, 'file_list.txt')
        os.rename('file_list.txt', output_file_path)

        print(f"File list saved to: {output_file_path}")
