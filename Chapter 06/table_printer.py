#! python3
# This is a table printer

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(data):
    # initalize the list "col_widths" with zeroes equal to the length of input
    col_width = [0] * len(data)
    
    for x in range(len(data)):
        for y in range(len(data[x])):
            if len(data[x][y]) > col_width[x]:
                col_width[x] = len(data[x][y])

    for a in range(len(data[0])):
        for b in range(len(data)):
            print(data[b][a].rjust(col_width[b]), end = ' ')
        print('')

print_table(table_data)
