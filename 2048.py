import random
print("welcome to 2048!")
print("developed by: @leokng-png")
def print_board(board):
    print("_" * 21)
    for row in board:
        ligne = "|"
        for num in row:
            ligne += f"{num:^4}|"
        print(ligne)
        print("_" * 21)
def empty_cells(board):
    empty = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty.append((i, j))
    return empty
def add_tile(board):
    empty = empty_cells(board)
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 2 if random.random() < 0.9 else 4
def compress(row):
    new_row =[]
    for num in row:
        if num != 0:
            new_row.append(num)
    while len(new_row) < 4:
        new_row.append(0)
    return new_row
def merge(row):
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row
def move_row_left(row):
    row = compress(row)
    row = merge(row)
    row = compress(row)
    return row
def move_left(board):
    new_board = []
    for row in board:
        new_row = move_row_left(row)
        new_board.append(new_row)
    return new_board
def move_right(board):
    new_board =[]
    for row in board:
        new_row = move_row_left(row[::-1])[::-1]
        new_board.append(new_row)
    return new_board
def move_up(board):
    transposed = [list(row) for row in zip(*board)]
    new_transposed = move_left(transposed)
    new_board = [list(row) for row in zip(*new_transposed)]
    return new_board
def move_down(board):
    transposed = [list(row) for row in zip(*board)]
    new_transposed = move_right(transposed)
    new_board = [list(row) for row in zip(*new_transposed)]
    return new_board
def has_won(board):
    for row in board:
        if 2048 in row:
            return True
    return False
def has_lost(board):
    for row in board:
        if 0 in row:
            return False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1]:
                return False
    for j in range(4):
        for i in range(3):
            if board[i][j] == board[i + 1][j]:
                return False
    return True
moves = {
    'z': move_up,
    's': move_down,
    'q': move_left,
    'd': move_right
}
board = [[0]*4 for _ in range(4)]
for _ in range(2):
    add_tile(board)
print_board(board)
while True:
    touche = input("Ton mouvement (z/q/s/d) : ")
    if touche in moves:
        ancient_board = [row[:] for row in board]
        board = moves[touche](board)
        if board != ancient_board:
            add_tile(board)
            print_board(board)
        if has_won(board):
            print("You win!")
            break
        if has_lost(board):
            print("You lose!")
            break
