import re

def regex_strip(text, value=''):
    if value != '':
        strip = re.compile(r'^['+value+']*|['+value+'+]*$')
        stripped_string = strip.sub('',text)
        print(stripped_string)
    else:
        blank_regex = re.compile(r'^(\s)*|(\s)*$')
        stripped_string = blank_regex.sub('',text)
        print(stripped_string)


print('Please enter text to strip here.')
text = input()
print('''Please enter what you would like to strip below
(If you want to strip white space, please hit enter''')
value = input()
regex_strip(text, value)
