import os

def rename_files(directory):
    # Get list of files in the directory
    files = os.listdir(directory)
    
    # Sort files to ensure consistent renaming order
    files.sort()
    
    # Initialize a counter for renaming
    count = 1
    
    # Iterate over each file and rename
    for file_name in files:
        if os.path.isfile(os.path.join(directory, file_name)):
            file_ext = os.path.splitext(file_name)[1]
            
            new_name = f"file{count}{file_ext}"
            
            current_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_name)
            
            os.rename(current_path, new_path)
            
            count += 1

if __name__ == "__main__":
    directory = "."  
    rename_files(directory)
    print("Files renamed successfully!")
