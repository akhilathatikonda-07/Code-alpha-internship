import os
import shutil

# Source folder path
source_folder = "source_images"

# Destination folder path
destination_folder = "moved_images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in source folder
for file_name in os.listdir(source_folder):

    # Check if file is JPG
    if file_name.endswith(".jpg"):

        # Full file path
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move file
        shutil.move(source_path, destination_path)

        print(f"Moved: {file_name}")

print("All JPG files moved successfully!")