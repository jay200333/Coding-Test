dx = [0,-1,0,1]
dy = [-1,0,1,0]

for _ in range(10):
    t = int(input())
    graph = []
    success_flag = False
    start_x, start_y = 0, 0
    target_x, target_y = 0, 0
    for i in range(16):
        input_list = list(map(int,input()))
        graph.append(input_list)
        for j in range(len(input_list)):
            if graph[i][j] == 2:
                start_x, start_y = i, j
            if graph[i][j] == 3:
                target_x, target_y = i, j

    def dfs(x, y):
        global success_flag
        if x == target_x and y == target_y:
            success_flag = True
            return
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= 16 or ny >= 16: continue
            if graph[nx][ny] == 3 or graph[nx][ny] == 0:
                graph[nx][ny] = -1
                dfs(nx,ny)

    graph[start_x][start_y] = -1
    dfs(start_x, start_y)

    if success_flag:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
    
