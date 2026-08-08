T = int(input())
for t in range(1,T+1):
    cur = input().rstrip()
    count_x = cur.count('x')
    if count_x <= 7:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")