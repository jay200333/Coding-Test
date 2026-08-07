T = int(input())
for t in range(1, T+1):
    a, b, c, d = map(int,input().split())
    minute = b + d
    hour = a + c
    if minute >= 60:
        hour += 1
        minute %= 60
    if hour >= 12:
        hour %= 12
        if hour == 0:
            hour = 12
    print(f"#{t} {hour} {minute}")