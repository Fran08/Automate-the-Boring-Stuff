#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.

""" Usage
    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
    py.exe mcb.pyw <keyword> - Load keyword to clipboard.
    py.exe mcb.pyw list - Loads all keywords to clipboard.
    py.exe mcb.pyw delete <keyword> - Delete keyword from shelf
    py.exe mcb.pyw delete - Delete all keywords from shelf """


import sys, pyperclip, shelve

# Open new shelf file and save it inside a variable
mcb_shelf = shelve.open('mcb')

# Saves copied text in clipboard to keyword provided in argument to mcb_shelf
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

# Deletes keyword in argument if it exists in mcb_shelf
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
        del mcb_shelf[sys.argv[2]]

# Checks if argument's length is 2
elif len(sys.argv) == 2:
    # Lists keywords if argument passed is list
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))

    # Copies values in keyword passed in argument if it exists to the clipboard
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

    # For loop that iterates through every keyword in mcb_shelf and deletes
    elif sys.argv[1] == 'delete':
        for keywords in list(mcb_shelf.keys()):
            del mcb_shelf[keywords]

mcb_shelf.close()
