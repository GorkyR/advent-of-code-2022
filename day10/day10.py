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
        match instruction:
            case ['noop']:
                pointer += 1
            case ['addx', value]:
                executing = int(value)
    else:
        register += executing
        executing = None
        pointer += 1

    if pointer >= len(instructions):
        break

print(sum(signal_strength_sample))
print('\n'.join(crt[i*40:(i+1)*40] for i in range(6)))


# BONUS!
letters = {
    'A': [
        '░██░',
        '█░░█',
        '█░░█',
        '████',
        '█░░█',
        '█░░█',
    ],
    'B': [
        '███░',
        '█░░█',
        '███░',
        '█░░█',
        '█░░█',
        '███░',
    ],
    'C': [
        '░██░',
        '█░░█',
        '█░░░',
        '█░░░',
        '█░░█',
        '░██░',
    ],
    'D': [
        '███░',
        '█░░█',
        '█░░█',
        '█░░█',
        '█░░█',
        '███░',
    ],
    'E': [
        '████',
        '█░░░',
        '███░',
        '█░░░',
        '█░░░',
        '████',
    ],
    'F': [
        '████',
        '█░░░',
        '███░',
        '█░░░',
        '█░░░',
        '█░░░',
    ],
    'G': [
        '░██░',
        '█░░█',
        '█░░░',
        '█░██',
        '█░░█',
        '░███',
    ],
    'H': [
        '█░░█',
        '█░░█',
        '████',
        '█░░█',
        '█░░█',
        '█░░█',
    ],
    'I': [
        '████',
        '░██░',
        '░██░',
        '░██░',
        '░██░',
        '████',
    ],
    'J': [
        '░░██',
        '░░░█',
        '░░░█',
        '░░░█',
        '█░░█',
        '░██░',
    ],
    'K': [
        '█░░█',
        '█░█░',
        '██░░',
        '█░█░',
        '█░█░',
        '█░░█',
    ],
    'L': [
        '█░░░',
        '█░░░',
        '█░░░',
        '█░░░',
        '█░░░',
        '████',
    ],
    'M': [
        '█░░█',
        '████',
        '██░█',
        '█░░█',
        '█░░█',
        '█░░█',
    ],
    'N': [
        '█░░█',
        '██░█',
        '██░█',
        '█░██',
        '█░██',
        '█░░█',
    ],
    'O': [
        '░██░',
        '█░░█',
        '█░░█',
        '█░░█',
        '█░░█',
        '░██░',
    ],
    'P': [
        '███░',
        '█░░█',
        '█░░█',
        '███░',
        '█░░░',
        '█░░░',
    ],
    'Q': [
        '░██░',
        '█░░█',
        '█░░█',
        '█░░█',
        '░██░',
        '░░░█',
    ],
    'R': [
        '███░',
        '█░░█',
        '█░░█',
        '███░',
        '█░█░',
        '█░░█',
    ],
    'S': [
        '░██░',
        '█░░█',
        '░█░░',
        '░░█░',
        '█░░█░',
        '░██░',
    ],
    'T': [
        '████',
        '░██░',
        '░██░',
        '░██░',
        '░██░',
        '░██░',
    ],
    'U': [
        '█░░█',
        '█░░█',
        '█░░█',
        '█░░█',
        '█░░█',
        '░██░',
    ],
    'V': [
        '█░░█',
        '█░░█',
        '█░░█',
        '█░░█',
        '████',
        '░██░',
    ],
    'W': [
        '█░░█',
        '█░░█',
        '█░░█',
        '██░█',
        '████',
        '█░░█',
    ],
    'X': [
        '█░░█',
        '█░░█',
        '░██░',
        '░██░',
        '█░░█',
        '█░░█',
    ],
    'Y': [
        '█░░█',
        '█░░█',
        '█░░█',
        '░██░',
        '░██░',
        '░██░',
    ],
    'Z': [
        '████',
        '░░░█',
        '░░█░',
        '░█░░',
        '█░░░',
        '████',
    ],
}

rows = [crt[i*40:i*40+40] for i in range(6)]
blocks = [[rows[j][i*5:i*5+4] for j in range(6)] for i in range(8)]
code = ''
for block in blocks:
    errors = []
    for letter, sprite in letters.items():
        error = sum(0 if sprite[i][j] == block[i][j]
                    else 1 for i in range(6) for j in range(4))
        errors.append((letter, error))
    code += min(errors, key=lambda x: x[1])[0]
print(code)
