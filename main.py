import math
import queue
import random

import pgzrun

"""CONFIGURATION"""

WIDTH = 800
HEIGHT = 800

"""VARIABLES"""

board_size = 40
delay = 5
wall_count = 120
start = (0, 0)
stop = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))

cell_size = WIDTH // board_size
board = []

"""DRAW"""


def draw():
    screen.fill((255, 255, 255))
    draw_board()


def draw_board():
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j]["vis"] == 1:
                screen.draw.filled_rect(board[i][j]["rect"], (0, 255, 0))
            elif board[i][j]["vis"] == 2:
                screen.draw.filled_rect(board[i][j]["rect"], (0, 0, 255))
            elif board[i][j]["vis"] == 3:
                screen.draw.filled_rect(board[i][j]["rect"], (120, 120, 120))
            elif board[i][j]["vis"] == 4:
                screen.draw.filled_rect(board[i][j]["rect"], (255, 0, 255))

            screen.draw.rect(board[i][j]["rect"], (0, 0, 0))

            screen.draw.text(str(int(board[i][j]["val"])),
                             center=(j * cell_size + cell_size / 2, i * cell_size + cell_size / 2))

    screen.draw.filled_rect(board[start[0]][start[1]]["rect"], (255, 100, 150))
    screen.draw.filled_rect(board[stop[0]][stop[1]]["rect"], (255, 0, 0))


"""UPDATE"""


def update():
    global board, wait, pq

    if pq.empty():
        return

    wait += 1
    wait %= delay

    if wait != 0:
        return

    _, i, j = pq.get()
    board[i][j]["vis"] = 1

    if i == stop[0] and j == stop[1]:
        pq = queue.PriorityQueue()
        mark_path()
        return

    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    # moves = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for mv in moves:
        ni = i + mv[0]
        nj = j + mv[1]
        if ni >= board_size or ni < 0 or nj >= board_size or nj < 0:
            continue

        if board[ni][nj]["vis"] != 0:
            continue

        val = manhattan_dist((ni, nj), stop)
        # val = euclidean_dist((ni, nj), stop)
        board[ni][nj]["vis"] = 2
        board[ni][nj]["val"] = val
        board[ni][nj]["prev"] = (i, j)
        pq.put((val, ni, nj))


"""EVENTS"""


def on_key_down(key):
    if key == keys.S:
        pq.put((0, start[0], start[1]))
    elif key == keys.R:
        init()


def on_mouse_down(pos):
    x, y = pos
    row, col = get_grid_pos(x, y)
    board[row][col]["vis"] = 3


"""HELPERS"""


def mark_path():
    current = board[stop[0]][stop[1]]["prev"]
    while current != start:
        board[current[0]][current[1]]["vis"] = 4
        current = board[current[0]][current[1]]["prev"]


def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_grid_pos(x, y):
    col = x // cell_size
    row = y // cell_size
    return row, col


"""INITIALIZATION"""


def init():
    global stop, pq, wait, board_size, wall_count, cell_size

    board_size = random.choice([5, 8, 10, 16, 50, 20, 40, 25, 32])
    wall_count = int(board_size ** 2 * 0.1)

    stop = (random.randint(0, board_size - 1),
            random.randint(0, board_size - 1))

    cell_size = WIDTH // board_size

    init_board()
    stop = (random.randint(0, board_size - 1),
            random.randint(0, board_size - 1))
    pq = queue.PriorityQueue()

    wait = 0


def init_board():
    global board

    board = [
        [{"rect": Rect((j * cell_size, i * cell_size), (cell_size, cell_size)), "val": 0, "vis": 0, "prev": (-1, -1)} for j in
         range(board_size)]
        for i in range(board_size)]

    for _ in range(wall_count):
        board[random.randint(0, board_size - 1)
              ][random.randint(0, board_size - 1)]["vis"] = 3


init()
pgzrun.go()
