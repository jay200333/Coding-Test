from itertools import combinations
T = int(input())
for t in range(1,T+1):
    cur = list(input().rstrip())
    min_value = int("".join(cur))
    max_value = int("".join(cur))
    target = []
    for i in range(len(cur)):
        target.append(i)
    for case in combinations(target, 2):
        x,y = case
        cur[x], cur[y] = cur[y], cur[x]
        if cur[0] == '0':
            cur[x], cur[y] = cur[y], cur[x]
            continue
        compare = int("".join(cur))
        min_value = min(min_value, compare)
        max_value = max(max_value, compare)
        cur[x], cur[y] = cur[y], cur[x]
    print(f"#{t} {min_value} {max_value}")