for t in range(1,11):
    n = int(input())
    heights = list(map(int,input().split()))
    answer = 0
    for i in range(2,n-2):
        temp = int(1e9)
        for j in range(-2,3):
            if j == 0: continue
            if heights[i+j] >= heights[i]:
                temp = 0
                break
            else:
                temp = min(temp,heights[i] - heights[i+j])
        answer += temp
    print(f"#{t} {answer}")