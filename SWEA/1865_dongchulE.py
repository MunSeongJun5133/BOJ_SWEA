import sys
sys.stdin = open("1865.txt", "r")

def find_best(depth, sum_v):
    global max_v

    if max_v >= sum_v:
        return

    if depth == N:
        max_v = max(max_v, sum_v)

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_best(depth + 1, sum_v * (percent[depth][i] / 100))
            visited[i] = 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    # print(percent)
    visited = [0] * N
    max_v = 0
    find_best(0, 1)

    print(f'#{t} {max_v * 100:.6f}')