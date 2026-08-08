T = int(input())
for t in range(1,T+1):
    a,b = map(int,input().split())
    temp = b * 2 + 1
    if a % temp != 0:
        result = (a // temp) + 1 
    else:
        result = a // temp
    print(f"#{t} {result}")