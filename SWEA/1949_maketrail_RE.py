import sys
sys.stdin = open("1949.txt", "r")
from collections import deque

def dfs(row, col, sum_v):
    global max_v, H, cnt

    max_v = max(max_v, sum_v)

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                if map_arr[nr][nc] < map_arr[row][col]:
                    visited[nr][nc] = 1
                    dfs(nr, nc, sum_v + 1)
                    visited[nr][nc] = 0

                elif map_arr[nr][nc] >= map_arr[row][col] and (map_arr[nr][nc] - K < map_arr[row][col]) and cnt == 0:
                    visited[nr][nc] = 1
                    cnt += 1
                    temp = map_arr[nr][nc]
                    map_arr[nr][nc] = map_arr[row][col] - 1
                    dfs(nr, nc, sum_v + 1)
                    cnt -= 1
                    map_arr[nr][nc] = temp
                    visited[nr][nc] = 0

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(map_arr)
    highest = deque()
    H = max(max(row) for row in map_arr)
    max_v = 0
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    # print(H)

    for row in range(N):
        for col in range(N):
            if map_arr[row][col] == H:
                highest.append((row, col))

    while highest:
        sr, sc = highest.popleft()
        visited[sr][sc] = 1
        dfs(sr, sc, 1)
        visited[sr][sc] = 0

    print(f"#{t} {max_v}")