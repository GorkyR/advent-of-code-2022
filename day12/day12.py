from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

grid = [list(line) for line in input.splitlines()]

start = next((row.index('S'), r) for r, row in enumerate(grid) if 'S' in row)
goal = next((row.index('E'), r) for r, row in enumerate(grid) if 'E' in row)

grid = [[0 if item == 'S' else 26 if item == 'E' else ord(item) - ord('a')
         for item in row] for row in grid]


def neighbors(point):
    return [(point[0] + x, point[1] + y) for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]]


def in_bounds(point, grid):
    height = len(grid)
    width = len(grid[0])
    return point[0] >= 0 and point[1] >= 0 and point[0] < width and point[1] < height


def min_disjkstra(goal, grid, predicate):
    open = {goal}
    closed = set()

    path_distance_field = [[float('inf') for _ in range(
        len(grid[0]))] for _ in range(len(grid))]
    path_distance_field[goal[1]][goal[0]] = 0

    while open:
        point = min(open, key=lambda p: path_distance_field[p[1]][p[0]])
        point_cost = path_distance_field[point[1]][point[0]]

        if predicate(point):
            return point_cost

        open.remove(point)
        closed.add(point)

        for n in filter(lambda n: in_bounds(n, grid), neighbors(point)):
            if n in closed or grid[point[1]][point[0]] - grid[n[1]][n[0]] > 1:
                continue
            open.add(n)
            cost = point_cost + 1
            prev_cost = path_distance_field[n[1]][n[0]]
            if cost < prev_cost:
                path_distance_field[n[1]][n[0]] = cost
    return None


print(min_disjkstra(goal, grid, lambda p: p == start))
print(min_disjkstra(goal, grid, lambda p: not grid[p[1]][p[0]]))
