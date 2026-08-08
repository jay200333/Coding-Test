for _ in range(10):
    t = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    answer = 0
    # 대각선 합
    sum_line1 = 0
    sum_line2 = 0
    
    for i in range(100):
        answer = max(answer, sum(board[i]))
        col_sum = 0
        for j in range(100):
            col_sum += board[j][i]
            if i == j:
                sum_line1 += board[i][j]
            elif i+j == 99:
                sum_line2 += board[i][j]
        answer = max(answer, col_sum)
    answer = max(answer, sum_line1, sum_line2)
    print(f"#{t} {answer}")