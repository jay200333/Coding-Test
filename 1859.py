T = int(input())
for t in range(1,T+1):
    n = int(input())
    prices = list(map(int,input().split()))
    answer = 0
    
    max_price = 0
    for price in reversed(prices):
        if max_price > price:
            answer += max_price - price
        else:
            max_price = price
    print(f"#{t} {answer}")
    