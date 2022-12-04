with open('./day1/input.txt', 'r') as file:
    input = file.read()

inventories = [inv.splitlines() for inv in input.split('\n\n')]
calories = [sum([int(cal) for cal in inv]) for inv in inventories]

print('top', max(calories))
print('top 3', sum(sorted(calories)[-3:]))
