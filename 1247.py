T = int(input())
for t in range(1,T+1):
    n = int(input())
    position = list(map(int,input().split()))
    company = (position[0], position[1])
    house = (position[2], position[3])
    position = [(position[i], position[i+1]) for i in range(4, len(position), 2)]
    visited = [False] * n
    answer = int(1e9)
    
    def calculateDistance(start, end):    
        return abs(start[0] - end[0]) + abs(start[1] - end[1])
            
    def backtrack(cur, count, dist):
        global answer
        if dist >= answer:
            return
        
        if count == n:
            answer = min(answer, calculateDistance(cur, house) + dist)
            return
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                backtrack(position[i], count+1, dist + calculateDistance(cur, position[i]))
                visited[i] = False
    
    backtrack(company, 0, 0)
    print(f"#{t} {answer}")