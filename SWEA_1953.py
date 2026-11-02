from collections import deque
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
tunnel_dir = {
    1: [0, 1, 2, 3],  # 상, 하, 좌, 우
    2: [0, 1],        # 상, 하
    3: [2, 3],        # 좌, 우
    4: [0, 3],        # 상, 우
    5: [1, 3],        # 하, 우
    6: [1, 2],        # 하, 좌
    7: [0, 2]         # 상, 좌
}
 
opposite = {0: 1, 1: 0, 2: 3, 3: 2}
 
T = int(input())
for t in range(1, T+1):
    n, m, r, c, l = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
 
    queue = deque([(r,c)])
    visited[r][c] = True
    time = 1
 
    while queue and time < l:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            cur_tunnel = graph[x][y]
            for i in tunnel_dir[cur_tunnel]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
                if visited[nx][ny] or graph[nx][ny] == 0: continue
                next_tunnel = graph[nx][ny]
 
                if opposite[i] in tunnel_dir[next_tunnel]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
        time += 1
 
    answer = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                answer += 1
 
    print(f"#{t} {answer}")
  
