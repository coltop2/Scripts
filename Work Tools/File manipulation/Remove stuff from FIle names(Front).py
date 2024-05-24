import os


def remove_characters_from_filenames(folder_path, num_chars):
    try:
        # Get a list of all files in the folder
        files = os.listdir(folder_path)

        # Filter PNG files
        png_files = [file for file in files if file.lower().endswith('.png')]

        # Set to store new file names and avoid duplicates
        new_names = set()

        # Generate new file names
        for file in png_files:
            new_name = file[num_chars:]

            # Check if the new name already exists, if not, add it to the set
            if new_name not in new_names:
                new_names.add(new_name)
            else:
                print(f"File '{new_name}' already exists in the folder.")

        # Rename files
        for file, new_name in zip(png_files, new_names):
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

        print(f"{len(png_files)} PNG files renamed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Prompt user for folder path and number of characters to remove
folder_path = input("Enter the folder path: ")
num_chars = int(input("Enter the number of characters to remove: "))

# Call the function
remove_characters_from_filenames(folder_path, num_chars)
