import os
def move(y, x, kto, board):
    if x.isdigit() and y.isdigit():
        x = x
    else: return False
    x,y=int(x),int(y)
    if 3 < x or x < 0 or 3 < y or y < 0:
        return False
    if board[y-1][x-1] == " ":
        board[y-1][x-1] = kto
        return True
    else:
        return False
def draw(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
def winning(board):
    for i in board:
        if i[1] == i[2] == i[0] != " ":
            return True
    for i in range(2, -1, -1):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    for i in range(0, 4, 2):
        if board[0][i-0] == board[1][i-1] == board[2][i-2] != " ":
            return True
    return False
def logic():
    turn="o"
    nturn="x"
    board = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]
    for i in range(9):
        
        os.system("cls")
        draw(board)
        pc = False
        while pc != True:
            print(turn+"s turn")
            pc = move(input("row"), input("column"), turn, board)
        if winning(board):
            os.system("cls")
            draw(board)
            print(turn + " is cool")
            input("New game")
            logic()
        nturn, turn = turn, nturn
        if i == 9:
            print("draw XD get gud")
            input("New game")
            logic()










logic()
#        |   |
#      --|---|--
#        |   |
#      --|---|--
#        |   |

# MOZE poTEM SZACHY?????