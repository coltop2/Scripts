from PIL import Image
import os
import shutil
import time


def resize_images_in_folder(folder_path, resize_percentage):
    # Create a new folder for resized images
    resized_folder = folder_path + "_" +  str(resize_percentage) + "%_Resized"
    os.makedirs(resized_folder, exist_ok=True)

    # Count total number of PNGs and JPGs in the folder
    total_images = sum(1 for filename in os.listdir(folder_path) if filename.endswith(('.jpg', '.png')))

    # Traverse the folder structure and resize images
    start_time = time.time()

    completed_images = 0

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                completed_images += 1
                image_path = os.path.join(root, filename)
                relative_path = os.path.relpath(image_path, folder_path)
                resized_relative_folder = os.path.join(resized_folder, relative_path)
                os.makedirs(os.path.dirname(resized_relative_folder), exist_ok=True)

                image = Image.open(image_path)

                # Calculate new size based on the resize percentage
                width, height = image.size
                new_width = int(width * resize_percentage / 100)
                new_height = int(height * resize_percentage / 100)

                # Resize the image
                resized_image = image.resize((new_width, new_height))

                # Save the resized image
                resized_image_path = os.path.join(resized_folder, relative_path)
                resized_image.save(resized_image_path)

                print(f"{completed_images}/{total_images} complete - Resized image saved: {resized_image_path}")

    end_time = time.time()
    duration = end_time - start_time
    print(f"Resizing completed in {duration:.2f} seconds.")


# Prompt the user for the folder path and resize percentage
folder_path = input("Enter the folder path: ")
resize_percentage = float(input("Enter the resize percentage (e.g., 50 for 50%): "))

# Call the function to resize images
resize_images_in_folder(folder_path, resize_percentage)
