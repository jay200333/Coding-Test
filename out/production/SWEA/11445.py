T = int(input())
for t in range(1,T+1):
    p = input().rstrip()
    q = input().rstrip()
    if p + 'a' == q:
        print(f"#{t} N")
    else:
        print(f"#{t} Y")