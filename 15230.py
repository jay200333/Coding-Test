T = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
for t in range(1,T+1):
    cur = input().rstrip()
    count = 0
    for i in range(len(cur)):
        if alpha[i] == cur[i]:
            count += 1
        else:
            break
    print(f"#{t} {count}")