import sys
sys.stdin = open("1859.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    sale_prices = list(map(int, input().split()))
    # print(sale_prices)
    max_v = max(sale_prices)
    purchase = 0
    sale = 0
    cnt = 0
    margin = 0

    if sale_prices[0] == max_v:
        print(f'#{t} {margin}')
        continue

    for i in range(N):
        today = sale_prices[i]

        if today != max_v:
            purchase += today
            cnt += 1

        elif today == max_v:
            sale = today * cnt
            margin += (sale - purchase)
            sale = 0
            purchase = 0
            cnt = 0
            if i != N - 1:
                max_v = max(sale_prices[i + 1:N])
            else:
                max_v = 0

    print(f'#{t} {margin}')
