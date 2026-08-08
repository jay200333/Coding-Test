T = int(input())
for t in range(1,T+1):
    n = int(input())
    result = 1
    temp_a = 0
    for i in range(1,n):
        for j in range(1,n):
            temp = i ** 2 + j ** 2
            if temp <= n**2:
                temp_a += 1
    result += (temp_a * 4)
    result += (n * 4)
    print(f"#{t} {result}")