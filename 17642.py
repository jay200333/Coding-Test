T = int(input())
for t in range(1,T+1):
    a,b = map(int,input().split())
    temp = b - a
    result = 0
    if temp == 1 or a > b:
        result = -1
    else:
        if temp % 2 == 1:
            temp -= 3
            result += 1
        result += (temp // 2)
    print(f"#{t} {result}")