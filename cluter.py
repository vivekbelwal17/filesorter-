import os 
import shutil

folder_path = r"C:\Users\vivek\Downloads"

all_items = os.listdir(folder_path)
print(f"DEBUG: I found these items: {all_items}")


print("starting the clean up process...\n")

for item in all_items:
    # 1. Verify we are only looking at files, not folders
    if os.path.isfile(os.path.join(folder_path, item)):
        filename, extension = os.path.splitext(item)
        
        if extension == ".py":
            continue 
        
        # 2. Determine the proper folder name (Properly indented!)
        if extension.lower() in [".jpg", ".jpeg", ".png"]:
            folder_name = "screenshots" # Fixed the variable name here
        elif extension:
            folder_name = extension[1:]  
        else:
            folder_name = "others"
            
        # 3. Create the folder and move the file (Properly indented!)
        target_folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)  
            
        source = os.path.join(folder_path, item)
        destination = os.path.join(target_folder, item)
        
        shutil.move(source, destination)
        print(f"Moved: '{item}' into the '{folder_name}' folder.")

print("\ncleanup completed.")