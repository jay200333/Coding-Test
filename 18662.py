T = int(input())
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    temp = numbers[2] - numbers[1]
    temp2 = numbers[1] - numbers[0]
    if temp == temp2:
        result = 0
    else:
        if temp > temp2:
            result = temp - temp2
        else:
            result = temp2 - temp
    result = result / 2
    print(f"#{t} {result}")