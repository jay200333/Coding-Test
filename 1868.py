import sys
input = sys.stdin.readline

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def check(curX,curY):
    visited[curX][curY] = True
    mine_count = countMine(curX,curY)
    graph[curX][curY] = mine_count
    if mine_count == 0:
        for i in range(8):
            nx = dx[i] + curX
            ny = dy[i] + curY
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if not visited[nx][ny] and graph[nx][ny] == '.':
                check(nx,ny)
                        
                        
def countMine(curX,curY):
    count = 0
    for i in range(8):
        nx = dx[i] + curX
        ny = dy[i] + curY
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if graph[nx][ny] == '*':
            count+=1
    return count

T = int(input())
for t in range(1,T+1):
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.' and countMine(i,j) == 0 and not visited[i][j]:
                check(i,j)
                answer += 1
            
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.' and not visited[i][j]:
                answer+=1
                
    print("#{0} {1}".format(t, answer))
        