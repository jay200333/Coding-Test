T = int(input())
for t in range(1,T+1):
    n, m = map(int,input().split())
    days = list(map(int,input().split()))
    short_term = sum(days[:m])
    long_term = sum(days[:m])
    cur_sum = sum(days[:m])
    for i in range(1, n-m+1):
        cur_sum = cur_sum - days[i-1] + days[i+m-1]
        short_term = min(short_term, cur_sum)
        long_term = max(long_term, cur_sum)
    print(f"#{t} {long_term - short_term}")