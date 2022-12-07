from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()


def start_of_message(message, count):
    for i in range(len(message) - (count - 1)):
        sub = set(message[i:i+count])
        if len(sub) == count:
            return i+count


print(start_of_message(input, 4))
print(start_of_message(input, 14))
