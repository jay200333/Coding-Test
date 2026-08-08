import copy

def rotate(graph):
    size = len(graph)
    temp_graph = copy.deepcopy(graph)
    for i in range(size):
        for j in range(size):
            temp_graph[i][j] = graph[size-j-1][i]
    return temp_graph


T = int(input())
for t in range(1, T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    answer = []
    
    for i in range(3):
        graph = rotate(graph)
        for i in range(n):
            answer.append("".join(map(str,graph[i])))
    
    print("#{0}".format(t))
    for i in range(n):
        for j in range(3):
            print(answer[j*n+i], end=" ")
        print()
    