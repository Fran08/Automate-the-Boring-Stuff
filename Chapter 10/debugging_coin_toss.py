# This program isn't meant to be intuitive and contains repition, but for
# the purpose of the debugging exercise, it will suffice.

import random, logging
#logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s \
- %(message)s')


logging.debug('Start of program.')
guess = ''


logging.debug('Toss coin and return heads of tails based on value 0 or 1')
toss = random.randint(0,1)
if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
logging.debug(f'The toss results is {toss}')


while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(f'Your current guess is {guess}')


if toss == guess:
    print('You got it!')
    logging.debug(f'The toss is {toss}. Your guess is {guess}.')

    
else:
    toss2 = random.randint(0,1)
    if toss2 == 0:
        toss2 = 'tails'
    elif toss2 == 1:
        toss2 = 'heads'
    logging.debug(f'The toss results is {toss2}')

    guess2 = ''
    while guess2 not in ('heads', 'tails'):
        print('Nope! Guess again! (heads or tails)')
        guess2 = input()
        logging.debug(f'Your current guess is {guess2}')
        
    if toss2 == guess2:
        print('You got it!')
        logging.debug(f'The toss is {toss2}. Your guess is {guess2}.')
    else:
        print('Nope. You are really bad at this game.')
        logging.debug(f'The toss is {toss2}. Your guess is {guess2}.')
