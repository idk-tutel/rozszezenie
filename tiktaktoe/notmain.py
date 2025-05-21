board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
def move(x, y, kto):
    if board[y-1][x-1] == " ":
        board[y-1][x-1] = kto
        return True
    else:
        return False
def draw():
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
def winning():
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
    for i in range(9):
        turn="o"
        draw()
        pc = False
        while pc != True:
            print(turn+"s turn")
            pc = move(int(input("row")), int(input("column")), turn)
        if winning():
            print(turn + " is cool")
            break
        if turn == "o":
            turn = "x"
        else: turn = "o"










logic()
#        |   |
#      --|---|--
#        |   |
#      --|---|--
#        |   |

# MOZE poTEM SZACHY?????