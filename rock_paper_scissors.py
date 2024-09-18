# We will write a rock paper scissors game in class - Complete it in this file

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " " , " "]

playerTurn = 1
winner = None

print("Input your moves with accordance to this: \n 1, 2, 3, \n 4, 5, 6, \n 7, 8, 9")

def drawBoard(board):
    return (f"{board[0]}, {board[1]}, {board[2]},\n{board[3]}, {board[4]}, {board[5]},\n{board[6]}, {board[7]}, {board[8]}")

def checkBoar(board):
    pass

while winner == None:

    try:
        move = int(input(f"Where would you like to go Player {playerTurn}? "))
    except:
        print("Input a integer.")

    while True:
        if move not in (1,2,3,4,5,6,7,8,9) or board[move - 1] != " ":
            move = int(input("Spot invalid or already taken. Try again. "))
        elif playerTurn == 1:
            board[move - 1] = "X"
            break
        elif playerTurn == 2:
            board[move - 1] = "O"
            break

    
    print(drawBoard(board))
    winner = 1