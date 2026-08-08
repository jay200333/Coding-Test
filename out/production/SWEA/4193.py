import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

T = int(input())
for t in range(1,T+1):
    n = int(input())
    graph = [list(map(int,input().split(" "))) for _ in range(n)]
    startX, startY = map(int,input().split(" "))
    targetX, targetY = map(int,input().split(" "))
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    visited[startX][startY] = 0
    queue.append((startX,startY))
    
    def bfs():
        answer = 0
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                curX, curY = queue.popleft()
                if (curX, curY) == (targetX, targetY):
                    return answer
            
                for i in range(4):
                    nx = dx[i] + curX
                    ny = dy[i] + curY
                    if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                    if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[curX][curY] + 1
                        queue.append((nx,ny))
                    elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
                        if answer % 3 == 2:
                            visited[nx][ny] = visited[curX][curY] + 1
                            queue.append((nx,ny))
                        else:
                            queue.append((curX,curY))
            answer+=1
        return -1
    
    ans = bfs()
    print("#{0} {1}".format(t,ans))
    