#! python3
# regex_search.py - Searches all .txt files in a folder and returns any line 
# that matches user-supplied text. Results found will print to screen.

import re, os

folder = os.path.abspath(input('Please enter folder to search: '))

if os.path.isdir(folder) is True:
    files = os.listdir(folder)
    txt_regex = re.compile(r'\w+\.txt', re.I)
    txt_files = txt_regex.findall(str(files))

    user_input = input('Please enter text to find: ')
    search_regex = re.compile(f'.*{user_input}.*')

    for file_num in range(len(txt_files)):
        file = open(os.path.join(folder, txt_files[file_num]))
        text = file.readlines()

        print(f'Results for: {txt_files[file_num]}')

        for lines in text:
            found = search_regex.search(lines)
            if found is None:
                continue
            else:
                print(found.group())
                
        file.close()
        
else:
    print('Folder does not exist.')
