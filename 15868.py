T = int(input())
for t in range(1,T+1):
    a,b = map(int,input().split())
    graph = []
    for _ in range(a):
        graph.append(list(map(int,input().rstrip())))
    flag = True
    for i in range(a):
        if sum(graph[i]) % 2 == 0:
            flag = False
            break
    if flag:
        result = "yes"
    else:
        result = "no"
    print(f"#{t} {result}")