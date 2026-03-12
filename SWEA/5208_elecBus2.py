import sys
sys.stdin = open("5208.txt", "r")

def find_min(depth, rest, count):
    global min_v

    if count >= min_v:
        return

    if depth == N - 1:
        min_v = min(min_v, count)
        return

    if rest > 0:
        find_min(depth + 1, rest - 1, count)
    find_min(depth + 1, M[depth] - 1, count + 1)

T = int(input())

for t in range(1, T + 1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1:]
    # print(N, M, rest)
    min_v = N

    find_min(1, M[0] - 1, 0)

    print(f'#{t} {min_v}')
