from collections import deque

T = int(input())
for t in range(1, T+1):
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [-1] * (n+1)
    visited[1] = 0
    answer = 0
    queue = deque([1])

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if visited[next] != -1: continue
            visited[next] = visited[cur] + 1
            queue.append(next)

    for i in visited:
        if i == 1 or i == 2:
            answer += 1
    print(f"#{t} {answer}")
