#! python3
# insert_gaps.py - This program insert gaps into numbered files so that a new file
# can be added. Note: To make sure program runs properly, there can't already be gaps
# in the folder. Run filling_gaps.py program first to close off all gaps.

import os, shutil, re

folder = os.path.abspath(input('Please enter folder to search: '))

if os.path.isdir(folder) is True:
    prefix = input('Enter file prefix: ')
    ext = input('Enter file extension: ')
    prefix_ext_regex = re.compile(f'({prefix})(\d+)\.({ext})', re.I)

    # Prompt user for location of file gap.
    # Number typed by user will be skipped.
    gap = input('Insert gap number (positive integer): ')
    count = 1
    
    if int(gap) > 0:
        for filename in os.listdir(folder):
            found = prefix_ext_regex.search(filename)
            if found:
                old_path = os.path.join(folder, filename)
                if found.group(2) == gap.zfill(len(found.group(2))):
                    count += 1
                new_filename = f'{found.group(1)}COPY{str(count).zfill(len(found.group(2)))}.{found.group(3)}'
                new_path = os.path.join(folder, new_filename)
                shutil.move(old_path, new_path)
                count += 1

        renamed_regex = re.compile(f'({prefix})COPY(\d+)\.({ext})', re.I)
        for filename in os.listdir(folder):
            found = renamed_regex.search(filename)
            if found:
                old_path = os.path.join(folder, filename)
                new_filename = f'{found.group(1)}{found.group(2)}.{found.group(3)}'
                new_path = os.path.join(folder, new_filename)
                shutil.move(old_path, new_path)
                
        print(f'{count - 1} files renamed')

    
    elif int(gap) < 0:
        print('Please enter a positive number')
    else:
        print('Please enter a valid integer')

    
else:
    print('Folder does not exist.')
