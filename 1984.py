T = int(input())
for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    totalSum = sum(numbers) - max(numbers) - min(numbers)
    answer = round(totalSum / 8)
    print(f"#{t} {answer}")