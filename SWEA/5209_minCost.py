import sys
sys.stdin = open("5209.txt", "r")

def find_min(depth, cost):
    global min_v

    if cost > min_v:
        return

    if depth == N:
        min_v = min(min_v, cost)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_min(depth + 1, cost + cost_comb[depth][i])
            visited[i] = 0

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cost_comb = [list(map(int, input().split())) for _ in range(N)]
    # print(cost_comb)
    min_v = 99 * N * N
    visited = [0] * N

    find_min(0, 0)

    print(f'#{t} {min_v}')