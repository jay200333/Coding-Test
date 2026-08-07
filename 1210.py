for i in range(10):
    t = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    
    def play(start_y):
        cur_x, cur_y = 0, start_y
        grid = [row[:] for row in board]
        
        while cur_x < 99:
            grid[cur_x][cur_y] = 0
            if cur_y - 1 >= 0 and grid[cur_x][cur_y - 1] == 1:
                cur_y -= 1
            elif cur_y + 1 < 100 and grid[cur_x][cur_y + 1] == 1:
                cur_y += 1
            else:
                cur_x += 1
        return grid[cur_x][cur_y] == 2
    
    for i in range(100):
        if board[0][i] == 1 and play(i):
            print(f"#{t} {i}")
            break
                