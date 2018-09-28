#! python3
# selective_copy.py - This program walks through a folder tree and searches
# for files with a certain file extension and copies them to new folder

import os, shutil, sys, re

folder = os.path.abspath(input('Please enter folder to search: '))

while True:
    if os.path.isdir(folder) is True:
        break
    else:
        print('Folder does not exist')
        sys.exit()


new_folder = os.path.abspath(input('Please enter new location to save: '))
if os.path.isdir(new_folder) is True:
    print('WARNING: Folder already exists, files with same names will be overwritten')
else:
    os.makedirs(new_folder)


ext = input('Please enter extension you are trying to copy:  ')
ext_regex = re.compile(f'\w+\.{ext}$', re.I)


i = 0
for foldername, subfolders, filenames in os.walk(folder):
    for file in filenames:
        if ext_regex.search(file):
            file_path = os.path.join(foldername, file)
            print(f'Copying {file} from {foldername}')
            shutil.copy(file_path, new_folder)
            i += 1

if i == 0:
    print('No files with that extension found')
elif i > 0:
    print(f'{i} files were successfully copied into {new_folder}')
