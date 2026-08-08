T = int(input())
for t in range(1,T+1):
    cur = input().rstrip()
    up, down = 1,1
    for i in range(len(cur)):
        if cur[i] == 'L':
            down = (up + down)
        elif cur[i] == 'R':
            up = (up + down)
    print(f"#{t} {up} {down}")