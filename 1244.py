T = int(input())
for t in range(1,T+1):
    num, count = input().split()
    visited = set()
    answer = 0

    def backtrack(cur_num_list, try_count):
        global answer
        if try_count == int(count):
            cur_num = int("".join(cur_num_list))
            answer = max(answer, cur_num)
            return

        state = ("".join(cur_num_list), try_count)
        if state in visited:
            return
        visited.add(state)

        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                next_list = cur_num_list[:]
                next_list[i], next_list[j] = next_list[j], next_list[i]
                backtrack(next_list, try_count+1)

    backtrack(list(num), 0)
    print(f"#{t} {answer}")
