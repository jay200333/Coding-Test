T = int(input())
for t in range(1, T+1):
    number_dict = {
    "ZRO" : 0,
    "ONE" : 0,
    "TWO" : 0,
    "THR" : 0,
    "FOR" : 0,
    "FIV" : 0,
    "SIX" : 0,
    "SVN" : 0,
    "EGT" : 0,
    "NIN" : 0
}
    c, n = input().split()
    orders = input().split()
    for i in range(int(n)):
        number_dict[orders[i]] += 1

    print(f"#{t}")
    for key, value in number_dict.items():
        if value > 0:
            print(" ".join([key] * value ), end=" ")    
    