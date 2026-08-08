
n = 100
isNotPrime = [False] * (n+1)
for i in range(2, n+1):
    if isNotPrime[i]: continue
    for j in range(4 * i, n+1, i):
        isNotPrime[j] = True

for i in range(2,n+1):
    if isNotPrime[i] == False:
        print(i, end=" ")