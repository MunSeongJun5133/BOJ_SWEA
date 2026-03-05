import sys
sys.stdin = open("14510.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tree_height = list(map(int, input().split()))
    # print(tree_height)
    big = max(tree_height)
    first_status = list()

    for h in tree_height:
        first_status.append(big - h)
    # print(first_status)

    day = list()

    even = 0
    odd = 0

    for h in first_status:
        even += h // 2
        odd += h % 2

    if even == 0 and odd == 0:
        print(f'#{t} {0}')
        continue

    while even >= 0:
        if even >= odd:
            day.append(even * 2)
        else:
            day.append(odd * 2 - 1)
        even -= 1
        odd += 2

    print(f'#{t} {min(day)}')