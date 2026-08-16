T = int(input())
for t in range(1, T+1):
    prices = list(map(int, input().split()))
    days = list(map(int, input().split()))

    totalDays = sum(days)
    totalMonths = sum(it > 0 for it in days)
    answer = min(prices[3], prices[1] * totalMonths, prices[0] * totalDays)

    def calculateBestOneMonthPrice(month_idx):
        return min(days[month_idx] * prices[0], prices[1])

    def dfs(month_idx, price):
        global answer
        
        if price >= answer:
            return

        if month_idx >= 12:
            answer = min(answer, price)
            return

        if days[month_idx] == 0:
            dfs(month_idx + 1, price)
            return

        month_cost = calculateBestOneMonthPrice(month_idx)
        dfs(month_idx + 1, price + month_cost)
        dfs(month_idx + 3, price + prices[2])

    dfs(0, 0)
    print(f"#{t} {answer}")