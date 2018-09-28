#! python3
# filling_gaps.py - This program finds files in a given prefix in a single folder
# and locates gaps in the numbering and renames all later files to close the gap.

import shutil, os, re

# COMMENTED OUT: Code is used to create 200 test files in this format "spamXXX.txt"
##for i in range(200):
##    doc = open(f'spam{str(i+1).zfill(3)}.txt', 'w')
##    doc.close()

folder = os.path.abspath(input('Please enter folder to search: '))

if os.path.isdir(folder) is True:
    prefix = input('Enter file prefix: ')
    ext = input('Enter file extension: ')
    prefix_ext_regex = re.compile(f'({prefix})(\d+)\.({ext})', re.I)

    count = 1

    for filename in os.listdir(folder):
        found = prefix_ext_regex.search(filename)
        if found:
            old_path = os.path.join(folder, filename)
            new_filename = f'{found.group(1)}{str(count).zfill(len(found.group(2)))}.{found.group(3)}'
            new_path = os.path.join(folder, new_filename)
            shutil.move(old_path, new_path)
            count += 1
            
    print(f'{count} files successfully renamed')
    
else:
    print('Folder does not exist.')
