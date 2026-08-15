def check(palindrome):
    count = 0
    for i in range(100):
        for j in range(i+1, 101):
            temp_string = palindrome[i:j]
            if temp_string == temp_string[::-1]:
                count = max(count, len(temp_string))
    return count

for t in range(1, 11):
    n = int(input())
    board = [list(input().strip()) for _ in range(100)]
    answer = 0
    for i in range(100):
        answer = max(answer, check(board[i]))
        column = []
        for j in range(100):
            column.append(board[j][i])
        answer = max(answer, check(column))
    print(f"#{n} {answer}")
