from collections import deque
T = int(input())
for t in range(1,T+1):
    q = deque()
    graph = []
    n = int(input())
    for i in range(n):
        graph.append(list(input().rstrip()))
        for j in range(n):
            if graph[i][j] == "#":
                q.append((i,j))
    count = len(q) ** 0.5
    if count % 1 != 0:
        print(f"#{t} no")
        continue
    flag = True
    x,y = q.popleft()
    for i in range(x, int(x + count)):
        for j in range(y,int(y + count)):
            if graph[i][j] != "#":
                flag = False
                break
    if flag:
        print(f"#{t} yes")
    else:
        print(f"#{t} no")