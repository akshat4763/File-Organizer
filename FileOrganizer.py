import os
import shutil

path = input("Enter the path of the folder you want to organize: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot from the extension

    if extension:
        # Create a subdirectory for the extension if it doesn't exist
        extension_dir = os.path.join(path, extension)
        os.makedirs(extension_dir, exist_ok=True)

        # Move the file to the subdirectory
        source_file = os.path.join(path, file)
        target_file = os.path.join(extension_dir, file)
        shutil.move(source_file, target_file)
        print(f"Moved {file} to {extension_dir}")
    else:
        print(f"Skipping {file} (no extension)")

print("Organizing completed.")
