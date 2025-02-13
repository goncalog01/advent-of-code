from collections import Counter
from itertools import product
from operator import add

def solve(lines):
    board = set()
    for row, line in enumerate(lines):
        for col, elem in enumerate(line):
            if elem == '#':
                cell = 3 * [0,]
                cell[0], cell[1] = col, row
                board.add(tuple(cell))

    for _ in range(6):
        new_board = set()

        neighbour_counts = Counter()
        for cell in board:
            for delta in product(range(-1, 2), repeat=3):
                if delta != 3 * (0,):
                    neighbour_counts[tuple(map(add, cell, delta))] += 1

        for cell, count in neighbour_counts.items():
            if count == 3 or (cell in board and count == 2):
                new_board.add(cell)
        board = new_board

    return len(board)

with open('input.txt') as f:
    lines = f.read().splitlines()

print(solve(lines))