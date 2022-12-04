from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

pairs = [[[int(i) for i in ass.split('-')] for ass in pairs.split(',')]
         for pairs in input.splitlines()]


def compare(a, b):
    return 1 if a > b else -1 if b > a else 0


compared = [[compare(ass1[0], ass2[0]), compare(ass1[1], ass2[1])]
            for ass1, ass2 in pairs]

print(len([1 for _ in compared if abs(_[0] + _[1]) <= 1]))

print(len([1 for ass1, ass2 in pairs if not ((ass1[0] < ass2[0]
      and ass1[1] < ass2[0]) or (ass1[0] > ass2[1] and ass1[1] > ass2[1]))]))
