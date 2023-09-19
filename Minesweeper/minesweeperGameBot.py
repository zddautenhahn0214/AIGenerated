import random

# Constant values for the game
BOARD_SIZE = 10
NUM_MINES = 10

# Create a 2D list to represent the game board
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Randomly place the mines on the board
mines = random.sample(range(BOARD_SIZE * BOARD_SIZE), NUM_MINES)
for mine in mines:
    x, y = mine // BOARD_SIZE, mine % BOARD_SIZE
    board[x][y] = -1

# Calculate the number of mines surrounding each cell
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if board[i][j] == -1:
            continue
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (0 <= i + dx < BOARD_SIZE) and (0 <= j + dy < BOARD_SIZE) and (board[i + dx][j + dy] == -1):
                    board[i][j] += 1

# Function to check if a cell is safe to reveal
def is_safe(x, y):
    return (0 <= x < BOARD_SIZE) and (0 <= y < BOARD_SIZE) and (board[x][y] != -1)

# Function to get the number of mines surrounding a cell
def num_mines(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (0 <= x + dx < BOARD_SIZE) and (0 <= y + dy < BOARD_SIZE) and (board[x + dx][y + dy] == -1):
                count += 1
    return count

# Function to get the number of mines surrounding a cell
def num_safe(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if is_safe(x + dx, y + dy):
                count += 1
    return count

# Function to get a list of safe, uncovered cells surrounding a cell
def get_safe_neighbors(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0) and (dy == 0):
                continue
            if is_safe(x + dx, y + dy):
                neighbors.append((x + dx, y + dy))
    return neighbors

# Function to get a list of mines surrounding a cell
def get_mine_neighbors(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0) and (dy == 0):
                continue
            if (0 <= x + dx < BOARD_SIZE) and (0 <= y + dy < BOARD_SIZE) and (board[x + dx][y + dy] == -1):
                neighbors.append((x + dx, y + dy))
    return neighbors


#ran out of space, asked it to finishe it :
# Function to play a single turn of Minesweeper
def play_turn():
    # Iterate over all cells in the board
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # If the cell is already revealed, skip it
            if board[i][j] != 0:
                continue
            # If the cell has no safe neighbors, reveal it
            if num_safe(i, j) == 0:
                board[i][j] = -2
                continue
            # If the number of mines surrounding the cell is equal to the number of unknown neighbors, flag all unknown neighbors as mines
            unknown_neighbors = [n for n in get_safe_neighbors(i, j) if board[n[0]][n[1]] == 0]
            if len(unknown_neighbors) == num_mines(i, j):
                for n in unknown_neighbors:
                    board[n[0]][n[1]] = -3
                continue
            # If the number of flagged cells surrounding the cell is equal to the number of mines surrounding the cell, reveal all unknown neighbors
            flagged_neighbors = [n for n in get_mine_neighbors(i, j) if board[n[0]][n[1]] == -3]
            if len(flagged_neighbors) == num_mines(i, j):
                for n in unknown_neighbors:
                    board[n[0]][n[1]] = -2

# Function to play the entire game of Minesweeper
def play_game():
    # Play turns until the game is over
    while True:
        play_turn()
        # Check if the game is won
        if all(cell != 0 for row in board for cell in row):
            print("You won the game!")
            break
        # Check if the game is lost
        if any(cell == -2 for row in board for cell in row):
            print("You lost the game!")
            break

# Play the game
play_game()

