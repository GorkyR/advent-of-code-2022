with open('./day2/input.txt', 'r') as file:
    input = file.read()

move_points = {'X': 1, 'Y': 2, 'Z': 3}
counter_points = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}

rounds = [line.split(' ') for line in input.splitlines()]

points = [move_points[move] + counter_points[attack][move]
          for attack, move in rounds]

print(sum(points))

outcome_points = {'X': 0, 'Y': 3, 'Z': 6}
counter_moves = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'},
}

new_points = [outcome_points[outcome] + move_points[counter_moves[attack][outcome]]
              for attack, outcome in rounds]

print(sum(new_points))
