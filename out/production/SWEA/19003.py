T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    result1 = 0
    result2 = 0
    words = []
    for _ in range(N):
        cur = input().rstrip()
        words.append(cur)
    for word in words:
        if word[::-1] in words and word != word[::-1]:
            result1 += M
        elif word[::-1] == word:
            result2 = M
    answer = result1 + result2
    print(f"#{t} {answer}")