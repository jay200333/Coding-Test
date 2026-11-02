# 한 칸에 가장 많이 겹치는 수 구하기

T = int(input())
for t in range(1, T+1):
    n = int(input())
    rooms = [0] * 201
    
    for _ in range(n):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        start, end = (s + 1) // 2, (e + 1) // 2
        for i in range(start, end + 1):
            rooms[i] += 1
    answer = max(rooms)
    print(f"#{t} {answer}")
        