import heapq

# 프림 알고리즘

T = int(input())
for t in range(1, T+1):
    answer = 0
    cnt = 0
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    for _ in range(e):
        start, end, dist = map(int, input().split())
        graph[start].append((dist, end))
        graph[end].append((dist, start))
    
    # 거리, 현재 노드
    heap = [(0, 1)]
    
    while heap and cnt < v:
        dist, node = heapq.heappop(heap)
        if visited[node]: continue
        visited[node] = True
        answer += dist
        cnt += 1

        for next_dist, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_dist, next_node))
    print(f"#{t} {answer}")

# # 크루스칼 알고리즘
# import heapq

# T = int(input())
# for t in range(1, T+1):
#     answer = 0
#     edges = []
#     mst_edges = []
#     v, e = map(int,input().split())
#     parent = list(range(v+1))
#     def find(x):
#       if parent[x] == x:
#           return x
#       parent[x] = find(parent[x])
#       return find(parent[x])

#     def union(start, end):
#         start = find(start)
#         end = find(end)
#         if start == end:
#             return False
#         parent[end] = start
#         return True
    
#     for i in range(e):
#         start, end, dist = map(int,input().split())
#         edges.append((dist, start, end))

#     edges.sort(key= lambda x:x[0])

#     for i in range(e):
#         dist, start, end = edges[i]
#         if union(start, end) == False:
#             continue
#         else:
#             answer += dist
#             mst_edges.append((dist, start, end))
#             if len(mst_edges) == v - 1:
#                 break
#     print(f"#{t} {answer}")
