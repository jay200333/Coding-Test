arr = []
T = int(input())
for t in range(1,T+1):
    a,b,c,d = map(int,input().split())
    result = [0] * 101
    for x in range(a,b+1):
        result[x] += 1
    for y in range(c,d+1):
        result[y] += 1
    answer = result.count(2)
    if answer > 0:
        answer -= 1
    arr.append(answer)
for i,j in enumerate(arr):
    print(f"#{i+1} {j}")