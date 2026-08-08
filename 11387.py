T = int(input())
for t in range(1,T+1):
    D,L,N = map(int,input().split())
    damage = 0
    for i in range(N):
        damage += D*(i*L*0.01 + 1)
    print(f"#{t} {int(damage)}")