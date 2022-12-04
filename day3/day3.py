from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

shacks = input.splitlines()
compartments = [[shack[:len(shack)//2], shack[len(shack)//2:]]
                for shack in shacks]

shared = []
for first, second in compartments:
    for item in second:
        if item in first:
            shared.append(item)
            break

priorities = [ord(item) - ord('a') + 1 for item in shared]
priorities = [p + ord('z') - ord('A') + 1 if p < 1 else p for p in priorities]

print(sum(priorities))

groups = [shacks[i:i+3] for i in range(0, len(shacks), 3)]

badges = []
for first, second, third in groups:
    for item in third:
        if item in first and item in second:
            badges.append(item)
            break

priorities = [ord(item) - ord('a') + 1 for item in badges]
priorities = [p + ord('z') - ord('A') + 1 if p < 1 else p for p in priorities]

print(sum(priorities))
