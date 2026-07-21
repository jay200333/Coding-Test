T = int(input())
for t in range(1,T+1):
    n, b = map(int,input().split())
    heights = list(map(int,input().split()))
    heights.sort()

    answer = int(1e9)
    visited = [False] * n

    def back(cur,temp_sum):
        global answer
        if temp_sum >= b:
            gap = abs(temp_sum- b)
            answer = min(answer, gap)
            return

        for i in range(cur, n):
            if not visited[i]:
                visited[i] = True
                back(i, temp_sum + heights[i])
                visited[i] = False

    back(0, 0)
    print("#{0} {1}".format(t,answer))