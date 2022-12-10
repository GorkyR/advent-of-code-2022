from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

moves = [move.split() for move in input.splitlines()]
moves = [(dir, int(count)) for dir, count in moves]


def adjacent(p):
    return [(p[0] + i, p[1] + j) for i in range(-1, 2) for j in range(-1, 2)]


def sign(n):
    return 1 if n >= 0 else -1


def count_visited_last_knot(moves, rope_length):
    knots = [{'pos': (0, 0)}] + [{'pos': (0, 0), 'visited': {(0, 0)}}
                                 for i in range(rope_length)]
    for dir, count in moves:
        for _ in range(count):
            match dir:
                case 'U':
                    knots[0]['pos'] = (knots[0]['pos'][0],
                                       knots[0]['pos'][1] + 1)
                case 'R':
                    knots[0]['pos'] = (knots[0]['pos'][0] +
                                       1, knots[0]['pos'][1])
                case 'D':
                    knots[0]['pos'] = (knots[0]['pos'][0],
                                       knots[0]['pos'][1] - 1)
                case 'L':
                    knots[0]['pos'] = (knots[0]['pos'][0] -
                                       1, knots[0]['pos'][1])
            for i, knot in list(enumerate(knots))[1:]:
                lead = knots[i - 1]['pos']
                if lead not in adjacent(knot['pos']):
                    dx = lead[0] - knot['pos'][0]
                    dy = lead[1] - knot['pos'][1]
                    if not dx:
                        knot['pos'] = (knot['pos'][0], knot['pos'][1] + dy//2)
                    elif not dy:
                        knot['pos'] = (knot['pos'][0] + dx//2, knot['pos'][1])
                    else:
                        knot['pos'] = (knot['pos'][0] + sign(dx),
                                       knot['pos'][1] + sign(dy))
                    knot['visited'].add(knot['pos'])
    return len(knots[-1]['visited'])


print(count_visited_last_knot(moves, 1))
print(count_visited_last_knot(moves, 9))
