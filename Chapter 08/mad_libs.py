#! python3
# mad_libs.py - This is a Mad Libs program, Chapter 8 project of Automate the Boring Stuff

import re, os

file = input('Please enter path of txt file: ')

if os.path.exists(file):
    mad_libs = open(file)
    text = mad_libs.read()
    mad_libs.close()
    
    words = text.split()
    words_dict = {key: value for key, value in enumerate(words)}
    keywords_regex = re.compile(r'noun|verb|adjective|adverb', re.I)
                  
    for key,value in words_dict.items():
        for word in keywords_regex.findall(value):
            user_input = input(f'Enter {word.lower()}: ')
            words_dict[key] = user_input

    result = ' '.join(words_dict.values())
    print(result)
    new_file = open('mad_libs_result.txt', 'w')
    new_file.write(result)
    new_file.close()

else:
    print('File does not exist')
