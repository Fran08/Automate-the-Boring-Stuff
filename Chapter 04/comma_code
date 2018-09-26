spam = ['apples', 'bananas', 'tofu', 'cats', 'Fran']
bacon = [1,2,3,4,5,6,7,8,9]
ham = ['Fran']
empty = []

def comma_code(word_list):
    if word_list == []:
        print('You did not enter a valid list.')
    elif len(word_list) == 1:
        print(word_list[0])
    else:
        body = ', '.join(map(str, word_list[:-1]))
        new_string = f"{body},and {word_list[-1]}"
        print(new_string)

comma_code(spam)
comma_code(bacon)
comma_code(ham)
comma_code(empty)
