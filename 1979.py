T = int(input())
for t in range(1,T+1):
    n,k = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    answer = 0
    
    def check(numbers):
        count = 0
        temp = 0
        for i in range(n):
            if i == n-1 and numbers[i] == 1:
                temp += 1
                if temp == k:
                    count += 1
            if numbers[i] == 0:
                if temp == k:
                    count += 1
                temp = 0
            elif numbers[i] == 1:
                temp += 1
        return count
    
    for i in range(n):
        answer += check(board[i])
        column = []
        for j in range(n):
            column.append(board[j][i])
        answer += check(column)
    print(f"#{t} {answer}")