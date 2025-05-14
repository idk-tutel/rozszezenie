board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
def move(x, y, kto):
    if board[y][x] == " ":
        board[y][x] = kto
        return True
    else:
        return False
def draw():
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
def logic():
    for i in range(9):
        turn="o"
        draw()
        while pc != True:
            pc = move(input("row"), input("column"))










#        |   |
#      --|---|--
#        |   |
#      --|---|--
#        |   |

# MOZE poTEM SZACHY?????