import heapq

T = int(input())

for t in range(1, T+1):
    answer = 0
    edges = []
    mst_edges = []
    v, e = map(int,input().split())
    parent = [-1] * (v + 1)
    def find(x):
        if parent[x] == -1:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(s, e):
        s = find(s)
        e = find(e)
        if s == e:
            return False
        parent[e] = s
        return True
    
    for i in range(e):
        a, b, c = map(int,input().split())
        edges.append((c, (a, b)))

    edges.sort(key= lambda x:x[0])

    for i in range(e):
        cur = edges[i]
        s, e = cur[1]
        if union(s, e) == False:
            continue
        else:
            answer += int(cur[0])
            mst_edges.append(cur)
            if len(mst_edges) == v - 1:
                break
    print(f"#{t} {answer}")