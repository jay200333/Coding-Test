T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    answer = int(1e9)
    
    groupA = []

    def score(group):
        result = 0
        for i in range(len(group)):
            for j in range(len(group)):
                if i == j: continue
                result += board[group[i]][group[j]]
        return result
    
    def backtrack(idx):
        global answer
        if idx == n:
            groupB = list(set(range(n)) - set(groupA))
            scoreA = score(groupA)
            scoreB = score(groupB)
            answer = min(answer, abs(scoreA - scoreB))
            return
        
        if idx == 0:
            groupA.append(idx)
            backtrack(idx + 1)
            groupA.pop()
        else:
            groupA.append(idx)
            backtrack(idx+1)
            groupA.pop()
            
            backtrack(idx+1)
            
    backtrack(0)
    print(f"#{t} {answer}")