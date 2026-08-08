T = int(input())
for t in range(1,T+1):
    n = int(input())
    days = list(map(int,input().split()))
    result = int(1e9)
    for i in range(7):
        if days[i] == 1:
            index = i
            temp_result = 0
            temp_n = n
            while temp_n:
                if days[index] == 1:
                    temp_n -= 1
                temp_result += 1
                index = (index + 1) % 7
            result = min(result, temp_result)
    print(f"#{t} {result}")