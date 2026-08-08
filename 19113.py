from collections import deque
T = int(input())
for t in range(1,T+1):
    N = int(input())
    result = []
    costs = list(map(int,input().split()))
    costs.reverse()
    q = deque(costs)
    while q:
        cur = q.popleft()
        temp = cur * 3 // 4
        if temp in q:
            q.remove(temp)
            result.append(temp)
    result.sort()
    answer = " ".join(map(str,result))
    print(f"#{t} {answer}")