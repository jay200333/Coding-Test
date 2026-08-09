T = int(input())
for t in range(1,T+1):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for i in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = 0
    def dfs(cur):
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                dfs(next)

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            answer += 1

    print(f"#{t} {answer}")