T = int(input())
for t in range(1,T+1):
    n = int(input())
    result = []
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0:
            result.append((i,n//i))
    answer = []
    for x,y in result:
        temp = x + y - 2
        answer.append(temp)
    print(f"#{t} {min(answer)}")