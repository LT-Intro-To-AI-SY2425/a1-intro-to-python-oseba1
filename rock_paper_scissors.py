# Tic Tac Toe Game not rock paper sissors i cant read :(

# Initialize the board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

playerTurn = 1
winner = None

#print("Input your moves according to this:\n 1 | 2 | 3\n---|---|---\n 4 | 5 | 6\n---|---|---\n 7 | 8 | 9")

def drawBoard(board):
    return (f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{board[0]} | {board[1]} | {board[2]}\n"
            "--|---|--\n"
            f"{board[3]} | {board[4]} | {board[5]}\n"
            "--|---|--\n"
            f"{board[6]} | {board[7]} | {board[8]}")

def checkWinner(board):
    # Check rows, columns, and diagonals
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and not str(board[combo[0]]).isnumeric():
            return board[combo[0]]
    return None

while winner is None:
    print(drawBoard(board))
    
    move = int(input(f"Where would you like to go Player {playerTurn}? ")) - 1

    while True:
        if move not in range(9) or not str(board[move]).isnumeric():
            move = int(input("Spot invalid or already taken. Try again: ")) - 1
        else:
            if playerTurn == 1:
                board[move] = "X"
            else:
                board[move] = "O"
            break

    winner = checkWinner(board)

    if winner is None:
        playerTurn = 2 if playerTurn == 1 else 1

# Print final board and declare the winner
print(drawBoard(board))
if winner:
    print(f"Player {1 if winner == 'X' else 2} wins!")
else:
    print("It's a tie!")