import sys
sys.stdin = open("2117.txt", "r")
from collections import deque

def check(row, col, K):
    home_cnt = 0
    dist_limit = K - 1

    for i in range(row - dist_limit, row + dist_limit + 1):
        for j in range(col - dist_limit, col + dist_limit + 1):
            if 0 <= i < N and 0 <= j < N:
                if abs(row - i) + abs(col - j) <= dist_limit:
                    if map_arr[i][j] == 1:
                        home_cnt += 1

    result = (home_cnt * M) - ((K * K) + (K - 1) * (K - 1))
    return result

def dfs(row, col, K):
    global max_v

    result = check(row, col, K)

    if result < 0:
        return

    max_v = max(max_v, result)

    dfs(row, col, K + 1)

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(map_arr)
    home = deque()
    max_v = 0

    for row in range(N):
        for col in range(N):
            if map_arr[row][col] == 1:
                home.append((row, col))

    # print(home)

    while home:
        row, col = home.popleft()

        dfs(row, col, 1)

    print(f"#{t} {max_v}")