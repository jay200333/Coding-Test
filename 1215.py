for t in range(1, 11):
    n = int(input())
    board = [list(input().rstrip()) for _ in range(8)]
    answer = 0

    def check(string):
        count = 0
        for i in range(8 - n + 1):
            temp_string = string[i:i+n]
            if temp_string == temp_string[::-1]:
                count += 1
        return count

    for i in range(8):
        column = []
        answer += check(board[i])
        for j in range(8):
            column.append(board[j][i])
        answer += check(column)

    print(f"#{t} {answer}")