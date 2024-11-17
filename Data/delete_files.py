import os
import glob
from pathlib import Path

def delete_specific_tifs(start_path):
    # Count files that will be deleted
    files_to_delete = []
    
    # First pass - identify files
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.tif') and ('GFP' in file or 'TRANS' in file):
                full_path = os.path.join(root, file)
                files_to_delete.append(full_path)
    
    # If no files found, exit
    if not files_to_delete:
        print("No matching .tif files found")
        return
    
    # Show preview of files to be deleted
    print(f"\nFound {len(files_to_delete)} files to delete:")
    for file in files_to_delete:
        print(f"- {file}")
    
    # Ask for confirmation
    response = input("\nDo you want to proceed with deletion? (yes/no): ").lower()
    if response != 'yes':
        print("Operation cancelled")
        return
    
    # Perform deletion
    deleted_count = 0
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            deleted_count += 1
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    
    print(f"\nOperation complete. {deleted_count} files deleted.")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Starting in directory: {current_dir}")
    delete_specific_tifs(current_dir)