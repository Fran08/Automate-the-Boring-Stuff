#! python3
# bullet_point_adder.py - Adds bullet points to the start
# of each line of text in the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for line in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[line] = '* ' + lines[line] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)
