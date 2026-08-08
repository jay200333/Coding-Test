T = int(input())
ans = []
for _ in range(T):
    cards = [0,0,4,4,4,4,4,4,4,4,16,4]
    total = 52
    n = int(input())
    total -= n
    temp = 0
    for _ in range(n):
        cur = int(input())
        cards[cur] -= 1
        temp += cur
    count = 0
    for i in range(2,22-temp):
        count += cards[i]
    if total // 2 < count:
        ans.append("GAZUA")
    else:
        ans.append("STOP")
for x,y in enumerate(ans):
    print(f"#{x+1} {y}")