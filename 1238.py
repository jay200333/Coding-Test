from collections import deque

for t in range(1, 11):
    n, s = map(int,input().split())
    visited = {}
    graph = {}
    input_list = list(map(int, input().split()))
    for i in range(n//2):
        start = input_list[i*2]
        end = input_list[i*2 + 1]
        if start not in visited:
            visited[start] = 0
        if end not in visited:
            visited[end] = 0
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        cur = queue.popleft()
        if cur in graph:
            for next in graph[cur]:
                if visited[next] == 0:
                    visited[next] = visited[cur] + 1
                    queue.append(next)
    max_value = max(visited.values())
    answer_list = []
    for key in visited:
        if visited[key] == max_value:
            answer_list.append(key)
    answer_list.sort(reverse=True)
    print(f"#{t} {answer_list[0]}")
        