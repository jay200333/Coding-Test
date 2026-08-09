from collections import deque

for t in range(1, 11):
    v, e = map(int,input().split())
    graph_info = list(map(int,input().split()))
    graph = [[] for _ in range(v+1)]
    queue = deque()
    degree = [0] * (v+1)
    answer = []
    for i in range(e):
        start, end = graph_info[i*2], graph_info[i*2 + 1]
        graph[start].append(end)
        degree[end] += 1
    
    for i in range(1, v+1):
        if degree[i] == 0:
            queue.append(i)
    
    while queue:
        cur = queue.popleft()
        answer.append(cur)
        for next in graph[cur]:
            degree[next] -= 1
            if degree[next] == 0:
                queue.append(next)
    
    answer = " ".join(map(str, answer))
    print(f"#{t} {answer}")
    