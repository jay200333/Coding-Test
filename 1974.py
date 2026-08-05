T = int(input())
def check_row(board):
    for i in range(9):
        if len(set(board[i])) != 9:
            return False
    return True

def check_column(board):
    for i in range(9):
        temp_column = set()
        for j in range(9):
            temp_column.add(board[j][i])
        if len(temp_column) != 9:
            return False
    return True

def check_small_board(board):
    for i in range(3):
        for j in range(3):
            temp_board = set()
            for k in range(3):
                for l in range(3):
                    temp_board.add(board[i*3+k][j*3+l])
            if len(temp_board) != 9:
                return False
    return True

for t in range(1,T+1):
    answer = 0
    board = [ list(map(int,input().split())) for _ in range(9)]
    if check_row(board) and check_column(board) and check_small_board(board):
        answer = 1

    print(f"#{t} {answer}")