import os
import shutil

# Step 1: Define the target folder
# '.' represents the current directory (the folder where this Python file is saved)
folder_path = r"C:\Users\vivek\Downloads\mlnotebook screenshots"

# Step 2: Get a list of everything inside the folder
# os.listdir() acts like the computer's eyes, reading the names of all files and folders present.
all_items = os.listdir(folder_path)

print("Starting the cleanup process...\n")

# Step 3: Loop through every item found in the folder
for item in all_items:
    
    # We only want to move files, not folders that already exist!
    # os.path.isfile() checks to make sure the item is actually a file.
    if os.path.isfile(os.path.join(folder_path, item)):
        
        # Step 4: Split the filename and its extension (e.g., "photo.png" -> "photo" and ".png")
        filename, extension = os.path.splitext(item)
        
        # We want to ignore THIS Python script so it doesn't accidentally move itself!
        if extension == '.py':
            continue
            
        # Remove the dot from the extension to create a clean folder name (e.g., ".png" becomes "png")
        # If a file doesn't have an extension, we will put it in an "others" folder
        if extension:
            folder_name = extension[1:] 
        else:
            folder_name = "othersfiles"
            
        # Step 5: Check if a folder for this file type already exists
        # If it does not exist, we use os.makedirs() to create it.
        target_folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            
        # Step 6: Move the file into its new home!
        # We define the current location (source) and the new location (destination)
        source = os.path.join(folder_path, item)
        destination = os.path.join(target_folder, item)
        
        # shutil.move() does the actual physical moving of the file
        shutil.move(source, destination)
        print(f"Moved: '{item}' into the '{folder_name}' folder.")

print("\nCleanup complete! Your folder is now organized.")