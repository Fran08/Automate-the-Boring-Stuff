#! python3
# delete_files.py - Don't get misled by the program name, hah. This program
# lists the files in a folder tree larger than 100MB and prints them to the screen.

import os

folder = os.path.abspath(input('Please enter folder to search for files larger than 100MB:\n'))

if os.path.isdir(folder) is True:

    i = 0  # Placeholder for number of files found larger than 100MB
    
    for foldername, subfolders, filenames in os.walk(folder):
        
        for file in filenames:
            abs_path = os.path.abspath(foldername)
            full_path = os.path.join(foldername, file)
            file_size = os.path.getsize(full_path)

            if file_size > 100000000:
                i += 1
                print(full_path)
                
    print(f'{i} files found larger than 100MB')

else:
    print('Folder does not exist.')
