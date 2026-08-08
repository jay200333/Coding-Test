for _ in range(10):
    t = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    answer = 0
    # 대각선 합
    sum_line1 = 0
    sum_line2 = 0
    
    for i in range(100):
        answer = max(answer, sum(board[i]))
        col_sum = sum(board[j][i] for j in range(100))
        answer = max(answer, col_sum)
        
        sum_line1 += board[i][i]
        sum_line2 += board[i][99-i]
    
    answer = max(answer, sum_line1, sum_line2)
    print(f"#{t} {answer}")