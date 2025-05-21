class help:
    
    def winning(board):
        def row():
            for i in board:
                if i[1] == i[2] == i[0]:
                    return True
        def col():
            for i in range(2, 0):
                if board[0[i]] == board[1[i]] == board[2[i]]:
                    return 1
        def dig():
            for i in range(2, 1):
                pass