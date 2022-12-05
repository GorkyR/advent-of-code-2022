from sys import argv
from os.path import join as path, dirname as dir
from itertools import takewhile

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

rows = list(takewhile(lambda x: x, input.splitlines()))[:-1]
cells = ([[row[i:i+4].strip() for i in range(0, len(row) + 1, 4)]
         for row in rows])
original_columns = [[cells[row][col][1] for row in range(len(cells))
                     if cells[row][col]] for col in range(len(cells[0]))]

moves = [line.split(' ')[1::2]
         for line in input.splitlines()[len(rows)+2:]]
moves = [list(map(int, move)) for move in moves]

columns = [list(column) for column in original_columns]

for count, origin, destination in moves:
    columns[destination - 1] = \
        list(reversed(columns[origin-1][:count])) + columns[destination - 1]
    columns[origin-1] = columns[origin-1][count:]

print(''.join([columns[i][0] for i in range(len(columns))]))

columns = [list(column) for column in original_columns]

for count, origin, destination in moves:
    columns[destination - 1] = \
        list(columns[origin-1][:count]) + columns[destination - 1]
    columns[origin-1] = columns[origin-1][count:]

print(''.join([columns[i][0] for i in range(len(columns))]))
