T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    candies = list(map(int,input().split()))
    candies.sort()
    result = int(1e9)
    for i in range(N-K+1):
        temp = candies[i:i+K]
        result = min(result,temp[-1] - temp[0])
    print(f"#{t} {result}")