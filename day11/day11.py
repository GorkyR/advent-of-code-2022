from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

groups = [monkey.splitlines()[1:] for monkey in input.split('\n\n')]
properties = [[prop.split(':')[1].strip() for prop in props]
              for props in groups]


def monkeys():
    return [{
        'items': [int(item.strip()) for item in prop[0].split(',')],
        'op': prop[1].split()[-2:],
        'test': int(prop[2].split()[-1]),
        'when_true': int(prop[3].split()[-1]),
        'when_false': int(prop[4].split()[-1])
    } for prop in properties]


def business(monkeys, rounds, divide):
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey['test']

    count = [0 for _ in range(len(monkeys))]
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            for worry in monkey['items']:
                count[i] += 1
                match monkey['op'][0]:
                    case '+':
                        if monkey['op'][1] == 'old':
                            worry *= 2
                        else:
                            worry += int(monkey['op'][1])
                    case '*':
                        if monkey['op'][1] == 'old':
                            worry *= worry
                        else:
                            worry *= int(monkey['op'][1])
                if divide:
                    worry //= 3
                worry %= lcm
                if not (worry % monkey['test']):
                    monkeys[monkey['when_true']]['items'].append(worry)
                else:
                    monkeys[monkey['when_false']]['items'].append(worry)
            monkey['items'] = []
    a, b = sorted(count, reverse=True)[:2]
    return a * b


print(business(monkeys(), 20, True))
print(business(monkeys(), 10_000, False))
