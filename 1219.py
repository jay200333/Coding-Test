for _ in range(10):
    t, n = map(int,input().split())
    numbers = list(map(int,input().split()))
    graph = [[] for _ in range(100)]
    visited = [False] * 100
    for i in range(n):
        graph[numbers[i*2]].append(numbers[i*2+1])

    def dfs(v):
        global visited
        if v == 99:
            return
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                dfs(i)
        return

    dfs(0)
    visited[0] = True
    if visited[99]:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
