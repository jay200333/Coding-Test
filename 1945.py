numbers = [2, 3, 5, 7, 11]
T = int(input())
for t in range(1, T+1):
    n = int(input())
    countList = [0] * 5

    for i in range(4,-1,-1):
        while n % numbers[i] == 0:
            if n % numbers[i] == 0:
                countList[i] += 1
                n //= numbers[i]

    answer = " ".join(map(str, countList))
    print(f"#{t} {answer}")
