T = int(input())
for t in range(1,T+1):
    n = int(input())
    numbers = list(map(int,input().split()))
    result = 0
    for i in range(n-2):
        temp = numbers[i:i+3]
        if temp[1] != max(temp) and temp[1] != min(temp):
            result += 1
    print(f"#{t} {result}")