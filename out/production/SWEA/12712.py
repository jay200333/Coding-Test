T = int(input())

case_1_dx = [-1,0,1,0]
case_1_dy = [0,-1,0,1]
case_2_dx = [-1,-1,1,1]
case_2_dy = [-1,1,-1,1]

for t in range(1,T+1):
    n,m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(n):
            result1, result2 = graph[i][j], graph[i][j]
            for k in range(4):
                curX, curY = i,j
                for l in range(m-1):
                    nx = case_1_dx[k] + curX
                    ny = case_1_dy[k] + curY
                    if (nx < 0 or ny < 0 or nx >= n or ny >= n): break
                    result1 += graph[nx][ny]
                    curX, curY = nx,ny
                    
            for k in range(4):
                curX, curY = i,j
                for l in range(m-1):
                    nx = case_2_dx[k] + curX
                    ny = case_2_dy[k] + curY
                    if (nx < 0 or ny < 0 or nx >= n or ny >= n): break
                    result2 += graph[nx][ny]
                    curX, curY = nx, ny
            answer = max(answer,result1, result2)
            
    print("#{0} {1}".format(t,answer))   
            