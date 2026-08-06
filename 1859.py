T = int(input())
for t in range(1,T+1):
    n = int(input())
    prices = list(map(int,input().split()))
    answer = 0
    
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        print("cur idx", i)
        if max_price > prices[i]:
            answer += max_price - prices[i]
        else:
            max_price = prices[i]
    print(f"#{t} {answer}")
    