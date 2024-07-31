'''
Student Name: Hasini Jayasekara
Student ID: 165513235
'''

import os
import shutil
import sys

def main(target_dir):
    # Check if the specified directory exists
    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is not a valid directory.")
        return
    
    # Get the absolute path of the target directory
    target_dir_abs = os.path.abspath(target_dir)
    print(f"Target directory: {target_dir_abs}")

    # Create the backups directory if it doesn't exist
    backups_dir = os.path.join(target_dir_abs, 'backups')
    if not os.path.exists(backups_dir):
        os.makedirs(backups_dir)
        print(f"Created backups directory: {backups_dir}")

    # Walk through the directory and back up Python scripts
    for root, directories, filenames in os.walk(target_dir_abs):
        # Skip the backups directory
        if 'backups' in root:
            continue
        for file in filenames:
            if file.endswith('.py'):
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Construct the backup file path
                backup_path = os.path.join(backups_dir, file)
                # Copy the file to the backups directory
                shutil.copy2(file_path, backup_path)
                print(f"Copied {file_path} to {backup_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lab8e.py <directory>")
    else:
        main(sys.argv[1])
