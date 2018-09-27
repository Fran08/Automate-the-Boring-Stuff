#! python3
# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os


def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    # Make sure folder is absolute
    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the ZIP file.
    print(f'Creating {zip_filename}...')
    backup = zipfile.ZipFile(zip_filename, 'w')
    

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}')
        # Add the current folder to the ZIP file.
        backup.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue  # Don't backup the backup ZIP files.
            backup.write(os.path.join(foldername, filename))
    backup.close()

    print('Done.')


backup_to_zip('C:\\Users\\Frannie\\Documents\\delicious')
                
