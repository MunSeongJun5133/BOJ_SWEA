import sys
sys.stdin = open("5656.txt", "r")
from collections import deque

def gravity(arr):
    for col in range(W):
        stack = list()
        for row in range(H):
            if arr[row][col] != 0:
                stack.append(arr[row][col])
                arr[row][col] = 0

        for row in range(H - 1, -1, -1):
            if stack:
                arr[row][col] = stack.pop()
            else:
                break

def block_pang(current_map, r, c):
    q = deque()
    q.append((r, c, current_map[r][c]))
    current_map[r][c] = 0

    while q:
        row, col, distance = q.popleft()

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            for d in range(1, distance):
                nr = row + (d * dr)
                nc = col + (d * dc)

                if 0 <= nr < H and 0 <= nc < W:
                    if current_map[nr][nc] != 0:
                        q.append((nr, nc, current_map[nr][nc]))
                        current_map[nr][nc] = 0


def dfs(depth, current_map):
    global min_v

    count = 0
    for row in current_map:
        for i in range(len(row)):
            if row[i] != 0:
                count += 1

    if count == 0:
        min_v = count
        return

    if depth == N:
        min_v = min(min_v, count)
        return

    for col in range(W):
        for row in range(H):
            if current_map[row][col] != 0:
                copy_map = [row[:] for row in current_map]
                block_pang(copy_map, row, col)
                gravity(copy_map)
                dfs(depth + 1, copy_map)
                break

T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(H)]
    # print(map_arr)
    min_v = float('inf')

    dfs(0, map_arr)

    print(f"#{t} {min_v}")