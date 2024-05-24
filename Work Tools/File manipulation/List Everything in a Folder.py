import os

def list_files_and_folders(input_folder):
    with open('file_list.txt', 'w') as file:
        for item in os.listdir(input_folder):
            item_path = os.path.join(input_folder, item)
            if os.path.isfile(item_path):
                file.write(f'File: {item}\n')
            elif os.path.isdir(item_path):
                file.write(f'Folder: {item}\n')

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
