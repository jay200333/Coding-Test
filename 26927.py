from collections import defaultdict

T = int(input())
for t in range(1,T+1):
    n = int(input())
    counter = defaultdict(int)
    numbers = list(map(int,input()))
    for i in numbers:
        counter[i] += 1
    sorted_counter = sorted(counter, key=lambda x: (counter[x], x), reverse=True)
    print(f"#{t} {sorted_counter[0]} {counter[sorted_counter[0]]}")