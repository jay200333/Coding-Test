T = int(input())
for t in range(1,T+1):
    n,b = map(int,input().split())
    heights = list(map(int,input().split()))
    heights.sort()
    
    start, end = 0, 0
    answer = int(1e9)
    result = 0
    
    def ex():
        while True:
            if result <= b:
                result += heights[end]
                answer = min(answer, abs(b - result))
                if end + 1 >= n:
                    return
                end+= 1
            else:
                result -= heights[start]
                answer = min(answer, abs(b - result))
                if start + 1 >= n:
                    return
                start += 1
    ex()
    print("#{0} {1}".format(t,answer))