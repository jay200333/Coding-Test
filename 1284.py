T = int(input())
for t in range(1, T+1):
    p, q, r, s, w = map(int,input().split())
    costA = w * p
    costB = q if w <= r else q + (w-r) * s
    print(f"#{t} {min(costA, costB)}")