#! python3
# rename_dates.py - Renames American style dates MM-DD-YYYY to
# European style dates DD-MM-YYYY in the current working directory.

import os, re, shutil

american_date = re.compile(r'''
^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
''', re.VERBOSE)

# Loop over the files in the working directory.
for amer_filename in os.listdir('.'):
    found = american_date.search(amer_filename)

    # Skip files without a date.
    if found == None:
        continue

    # Get the different parts of the filename.
    before_date = found.group(1)
    month_date = found.group(2)
    day_date = found.group(4)
    year_date = found.group(6)
    after_date = found.group(8)

    # Form the European style filename.
    euro_filename = f'{before_date}{day_date}-{month_date}-{year_date}{after_date}'

    # Get the full, absolute file paths.
    abs_work_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_work_dir, amer_filename)
    euro_filename = os.path.join(abs_work_dir, euro_filename)

    # Rename the files.
    shutil.move(amer_filename, euro_filename)

