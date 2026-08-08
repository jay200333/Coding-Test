def GCD(a,b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

T = int(input())
for t in range(1,T+1):
    a,b = input().split()
    a_length = len(a)
    b_length = len(b)
   
    if a_length < b_length:
        temp, temp_length = a, a_length
        a, a_length = b, b_length
        b, b_length = temp, temp_length
    gcd = GCD(a_length, b_length)
    lab = a_length * b_length // gcd
    a = a * (lab // a_length)
    b = b * (lab // b_length)
    if a == b:
        print(f"#{t} yes")
    else:
        print(f"#{t} no")