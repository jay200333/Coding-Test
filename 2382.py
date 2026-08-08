from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def change_direction(direction):
    cur_direction = direction
    if direction == 1 or direction == 3:
        cur_direction += 1
    else:
        cur_direction -= 1
    return cur_direction

T = int(input())
for t in range(1,T+1):
    n,m,k = map(int,input().split())
    graph = [[[] for _ in range(n)] for _ in range(n)]
    queue = deque()
    for i in range(k):
        x,y,c,d = map(int,input().split())
        queue.append((x,y,c,d))
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                graph[i][j] = [(-1,-1)]
                
    for i in range(len(queue)):
        x,y,c,d = queue[i]
        graph[x][y] = [(c,d)]
    
    time = 0
    answer = 0
    while True:
        if time == m+1:
            break
        
        for i in range(len(queue)):
            cur_x,cur_y,cur_count,cur_dir = queue.popleft()
            nx = dx[cur_dir - 1] + cur_x
            ny = dy[cur_dir - 1] + cur_y
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                new_dir = change_direction(cur_dir)
                half_count = cur_count // 2
                if half_count == 0:
                    graph[nx][ny] = [(-1,-1)]
                else:
                    graph[nx][ny] = [(cur_count // 2, new_dir)]
            else:
                graph[cur_x][cur_y] = []
                graph[nx][ny].append((cur_count, cur_dir))
        
        for i in range(n):
            for j in range(n):
                info_list = graph[i][j]
                if len(info_list) == 1 and info_list[0][0] != -1:
                    queue.append((i, j, info_list[0][0], info_list[0][1]))
                elif len(info_list) >= 2:
                    sum_count = info_list[0][0]
                    max_info = info_list[0]
                    for k in range(1, len(info_list)):
                        if max_info[0] < info_list[k][0]:
                            max_info = info_list[k]
                        sum_count += info_list[k][0]
                    queue.append((i, j, sum_count, max_info[1]))
        
        time+=1
    
    for i in range(n):
        for j in range(n):
            info_list = graph[i][j]
            if len(info_list) == 1 and info_list[0][0] != -1:
                answer += info_list[0][0]
            elif len(info_list) >= 2:
                for k in range(len(info_list)):
                    answer += info_list[k][0]
    
    print(f"#{t} {answer}")
    