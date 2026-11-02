for t in range(1, 11):
    n = int(input())
    password = list(map(int,input().split()))
    count = int(input())
    orders = list(input().split("I"))
    for i in range(1, len(orders)):
        order_list = list(map(int,orders[i].split()))
        password[order_list[0] : order_list[0]] = order_list[2:]
    print(f"#{t}", *password[:10])
