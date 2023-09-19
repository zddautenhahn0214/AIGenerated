#chatGPT "write the game minesweeper in python"
import random
import tkinter as tk

# Constant values for the game
BOARD_SIZE = 10
NUM_MINES = 10

# Create a 2D list to represent the game board
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# Create the GUI
root = tk.Tk()
root.title("Minesweeper")

# Create a grid of buttons to represent the game board
buttons = [[tk.Button(root, width=2, height=1) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        def reveal(i, j):
            # Reveal the cell when the button is clicked
            if board[i][j] == -1:
                buttons[i][j].config(text="X", bg="red")
            else:
                buttons[i][j].config(text=board[i][j], bg="lightgrey")
            buttons[i][j]['state'] = 'disabled'
        buttons[i][j].config(command=lambda i=i, j=j: reveal(i, j))
        buttons[i][j].grid(row=i, column=j)



# Function to reset the game board
def reset_board():
    global board
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
    # Reset the buttons
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            buttons[i][j].config(text="", bg="white", state='normal')


# Add a reset button
reset_button = tk.Button(root, text="Reset", command=reset_board)
reset_button.grid(row=BOARD_SIZE, column=0, columnspan=BOARD_SIZE)

# Initialize the game board
reset_board()

# Run the GUI
root.mainloop()
