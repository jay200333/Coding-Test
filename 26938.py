T = int(input())
for t in range(1, T+1):
    e, n = map(int,input().split())
    graph = [[] for _ in range(e+2)]
    orders = list(map(int, input().split()))
    for i in range(0, len(orders), 2):
        if orders[i+1] == 0: continue
        graph[orders[i]].append(orders[i+1])
    answer = 0
    visited = [False] * (e+2)
    def dfs(v):
        global answer
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                answer += 1
                dfs(i)
    answer = 1
    visited[n] = True
    dfs(n)
    print(f"#{t} {answer}")
