from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

instructions = [ins.split() for ins in input.splitlines()]

signal_strength_sample = []
crt = ''

cycle = 0
pointer = 0
executing = None
register = 1
while True:
    cycle += 1

    if cycle == 20 or (cycle - 20) % 40 == 0:
        signal_strength_sample.append(cycle * register)

    ray = (cycle-1) % 40
    crt += '█' if ray >= register - 1 and ray <= register + 1 else '░'

    if executing is None:
        instruction = instructions[pointer]
        if instruction[0] == 'noop':
            pointer += 1
        if instruction[0] == 'addx':
            executing = int(instruction[1])
    else:
        register += executing
        executing = None
        pointer += 1

    if pointer >= len(instructions):
        break

# print(signal_strength_sample)
print(sum(signal_strength_sample))
print('\n'.join(crt[i*40:(i+1)*40] for i in range(6)))
