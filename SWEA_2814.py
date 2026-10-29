T = int(input())
for t in range(1, T+1):
  N, M = map(int, input().split())
  graph = [[] for _ in range(11)]
  for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
  visited = [False] * 11
  answer = 0

  def dfs(cur, count):
    temp = count
    for next in graph[cur]:
      if not visited[next]:
        visited[next] = True
        temp = max(dfs(next, count + 1), temp)
        visited[next] = False
    return temp

  for i in range(1, N+1):
      visited[i] = True
      answer = max(answer, dfs(i, 1))
      visited[i] = False
      if answer == N:
        break

  print(f"#{t} {answer}")
  
