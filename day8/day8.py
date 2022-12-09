from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

trees = [[int(col) for col in row] for row in input.splitlines()]


def map_over_cross(two_dim_list, transformer, collector):
    size = len(two_dim_list[0])
    output = []
    for row in range(size):
        output_row = []
        for col in range(size):
            element = two_dim_list[row][col]

            n = transformer(
                list(reversed([r[col] for r in two_dim_list[:row]])), element)
            w = transformer(list(reversed(two_dim_list[row][:col])), element)
            s = transformer([r[col] for r in two_dim_list[row+1:]], element)
            e = transformer(two_dim_list[row][col+1:], element)

            output_row.append(collector(element, n, w, s, e))
        output.append(output_row)
    return output


visibility = map_over_cross(trees, lambda l, _: max(l) if l else -1, lambda el,
                            n, w, s, e: 1 if min(n, w, s, e) < el else 0)
print(sum([sum(row) for row in visibility]))


def up_to_and_including(list, predicate):
    output = []
    for el in list:
        output.append(el)
        if predicate(el):
            return output
    return output


view_scores = map_over_cross(trees, lambda l, t: len(up_to_and_including(
    l, lambda x: x >= t)), lambda _, n, w, s, e: n * w * s * e)
print(max([max(row) for row in view_scores]))
