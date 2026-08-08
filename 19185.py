T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    first = list(input().split())
    second = list(input().split())
    result = []
    f_idx, s_idx = 0,0
    while True:
        f_idx = (f_idx) % N
        s_idx = s_idx % M
        temp = first[f_idx] + second[s_idx]
        if temp in result:
            break
        result.append(temp)
        f_idx += 1
        s_idx += 1
    K = int(input())
    answer = []
    for _ in range(K):
        c = int(input())
        c_temp = result[(c-1) % len(result)]
        answer.append(c_temp)
    last = " ".join(answer)
    print(f"#{t} {last}")