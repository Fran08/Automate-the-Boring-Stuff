#! python3
# strong_password.py - A strong password detector program

import sys, re

password = sys.argv[1]

if len(sys.argv[1]) < 8:
    print('Password needs to be at least 8 characters long.')
    sys.exit()

upper_regex = re.compile(r'[A-Z]+')
lower_regex = re.compile(r'[a-z]+')
digit_regex = re.compile(r'\d+')

if upper_regex.search(password) == None:
    print('You do not have an uppercase character in the password.')

elif lower_regex.search(password) == None:
    print('You do not have lowercase characters in the password.')

elif digit_regex.search(password) == None:
    print('You do not have at least one digit in the password.')

else:
    print('Password is strong.')
