T = int(input())
for t in range(1,T+1):
    n = int(input())
    temp = input().rstrip()
    flag = True
    if n % 2 == 0:
        half = n//2
        for i in range(half):
            if temp[i] != temp[i+half]:
                flag = False
                break
    else:
        flag = False
    if flag:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")