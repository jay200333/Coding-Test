T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    graph = []
    board = [0,0,0,0]
    for _ in range(N):
        graph.append(list(input().rstrip()))
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '#':
                if (i+j) % 2 == 0:
                    board[0] += 1
                else:
                    board[1] += 1
            elif graph[i][j] == ".":
                if (i+j) % 2 == 0:
                    board[2] += 1
                else:
                    board[3] += 1
    if (board[0] and board[1]) or (board[0] and board[2]) or (board[2] and board[3]) or (board[1] and board[3]):
        answer = "impossible"
    else:
        answer = "possible"
    print(f"#{t} {answer}")    