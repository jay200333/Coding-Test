T = int(input())
for t in range(1,T+1):
    candies = list(map(int,input().split()))
    candies.reverse()
    result = 0
    flag = True
    for i in range(2):
        if candies[i] > candies[i+1]:
            continue
        else:
            temp = candies[i] - 1
            if temp <=0:
                flag = False
                break
            result += candies[i+1] - temp
            candies[i+1] = temp
    if not flag:
        result = -1
    print(f"#{t} {result}")