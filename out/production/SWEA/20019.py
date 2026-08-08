T = int(input())
for t in range(1,T+1):
    N = input().rstrip()
    N_len = (len(N)-1) // 2
    flag1 = False
    flag2 = False
    flag3 = False
    temp = N[::-1]
    temp_1 = N[:N_len]
    temp_1 = temp_1[::-1]
    temp_2 = N[-N_len:]
    temp_2 = temp_2[::-1]
    if N == temp:
        flag1 = True
    if N[:N_len] == temp_1:
        flag2 = True
    if N[-N_len:] == temp_2:
        flag3 = True
    result = "NO"
    if flag1 and flag2 and flag3:
        result = "YES"
    print(f"#{t} {result}")