n,m = map(int, input().split())
arr = list(map(int,input().split()))
numbers = [0] * (n+1)
for i in range(1,n+1):
    numbers[i] = numbers[i-1] + arr[i-1]

for _ in range(m):
    a, b = map(int,input().split())
    print(numbers[b] - numbers[a-1])