def isPrime(num):
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())
for t in range(1,T+1):
    number = int(input())
    result = 3
    while True:
        if not isPrime(result) and not isPrime(result + number):
            print(f"#{t} {result+number} {result}")
            break
        result += 1