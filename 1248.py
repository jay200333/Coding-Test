def getPath(cur, target, path):
    path.append(cur)
    if cur == target:
        return True
    for i in parents[cur]:
        if getPath(i,target, path):
            return True
    path.pop()
    return False

def getSize(cur):
    if len(parents[cur]) == 0:
        return 1

    size = 1
    for i in parents[cur]:
        size += getSize(i)
    return size

T = int(input())
for t in range(1, T+1):
    v,e,a,b = map(int,input().split())
    parents = [[] for _ in range(v+1)]
    edge_list = list(map(int,input().split()))
    for j in range(e):
        parents[edge_list[j*2]].append(edge_list[j*2+1])

    first_path = []
    second_path = []
    
    getPath(1,a, first_path)
    getPath(1,b,second_path)
    
    common_node = 0
    
    for i in first_path[::-1]:
        if i in second_path:
            common_node = i
            break

    node_size = getSize(common_node)
    print(f"#{t} {common_node} {node_size}")