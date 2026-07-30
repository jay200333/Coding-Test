T = int(input())
for test in range(1,T+1):
    n, l = map(int,input().split())
    answer = 0
    food_list = []
    for i in range(n):
        t,k = map(int,input().split())
        food_list.append((t,k))    
    
    def backtrack(cur, score, total):
        global answer
        if total > l:
            return
                
        if cur == n:
            answer = max(answer, score)
            return
        
        backtrack(cur+1, score + food_list[cur][0], total + food_list[cur][1])
            
        backtrack(cur+1, score, total)
            
    backtrack(0, 0, 0)
    print(f"#{test} {answer}")
            