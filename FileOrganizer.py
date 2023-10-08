import os
import shutil

# Define the folder names for specific extensions
extension_folders = {
    "jpeg": "Images",
    "jpg": "Images",
    "png": "Images",
    "mp3": "Music",
    "mp4":"Videos",
    "txt": "Text",
    "pdf": "Pdf",
    "mkv": "Videos",
    "dmg": "Application",
    "docx": "Document",
    "zip": "Zip",
    "exe": "Application",
    "html": "Html",
    "css": "CSS",
    "py": "Python",
    "js": "Javascript",
    "webp": "Images",
    
}

# Function to create a directory for a specific extension and move files into it
def organize_by_extension(path, extension):
    extension_dir = os.path.join(path, extension_folders.get(extension, "Other"))
    os.makedirs(extension_dir, exist_ok=True)

    for file in os.listdir(path):
        if file.lower().endswith(f".{extension}"):
            source_file = os.path.join(path, file)
            target_file = os.path.join(extension_dir, file)
            shutil.move(source_file, target_file)
            print(f"Moved {file} to {extension_dir}")

# Main part of the code
path = input("**************** Welcome to File Organizer 2.0 ***************\nPlease enter the directory path you'd like to organize.\n: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if extension:
        # Call the function to organize files by extension
        organize_by_extension(path, extension)
    else:
        print(f"Skipping {file} (no extension)")

print("Organizing completed.")