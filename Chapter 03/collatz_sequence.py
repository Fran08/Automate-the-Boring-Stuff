# This program is the Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print('Hello, what is your name?')
name = input()

print(f'Hello {name}, please enter an integer: ')
try:
    value = int(input())
    while value != 1:
        value = collatz(value)
        print(value)

except ValueError:
    print('You must enter an integer...')
