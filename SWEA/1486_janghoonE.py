import sys
sys.stdin = open("1486.txt", "r")

def recur(k, sum_v):
    global min_v

    if sum_v >= min_v:
        return

    if k == N:
        if sum_v >= B and sum_v < min_v:
            min_v = sum_v

        return

    recur(k + 1, sum_v)
    recur(k + 1, sum_v + H[k])

T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    # print(N, B)
    # print(H)
    min_v = sum(H) + 1

    recur(0, 0)

    print(f'#{t} {min_v - B}')