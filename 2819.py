T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for t in range(1, T+1):
    board = [list(map(int,input().split())) for _ in range(4)]
    answer = 0
    number_set = set()
    def backTrack(cur, x, y):
        if len(cur) == 7:
            number_set.add(cur)
            return
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4: continue
            backTrack(cur+str(board[nx][ny]), nx, ny)
    
    for i in range(4):
        for j in range(4):
            backTrack(str(board[i][j]), i, j)
            
    print(f"#{t} {len(number_set)}")