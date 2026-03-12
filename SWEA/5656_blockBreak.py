import sys
sys.stdin = open("5656.txt", "r")
from collections import deque

def set_map(new_map):
    for col in range(W):
        STACK = list()
        for row in range(H):
            if new_map[row][col] != 0:
                STACK.append(new_map[row][col])
                new_map[row][col] = 0

        row = H - 1
        while STACK:
            new_map[row][col] = STACK.pop()
            row -= 1


def block_pang(r, c, new_map):
    q = deque()
    q.append((r, c, new_map[r][c]))
    new_map[r][c] = 0

    while q:
        row, col, R = q.popleft()

        if R == 0:
            continue

        new_map[row][col] = 0

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            for k in range(1, R):
                nr = row + (k * dr)
                nc = col + (k * dc)

                if 0 <= nr < H and 0 <= nc < W:
                    if new_map[nr][nc] > 1:
                        q.append((nr, nc, new_map[nr][nc]))
                        new_map[nr][nc] = 0
                    else:
                        new_map[nr][nc] = 0

    set_map(new_map)

def find_row(col, new_map):
    for row in range(H):
        if new_map[row][col] != 0:
            return row

    return -1

def dfs(depth, current_map):
    global min_v

    cnt = 0
    for row in range(H):
        for col in range(W):
            if current_map[row][col] != 0:
                cnt += 1

    if cnt == 0:
        min_v = 0
        return

    if depth == N:
        min_v = min(min_v, cnt)
        return

    for col in range(W):
        new_map = [row[:] for row in current_map]
        row = find_row(col, new_map)
        if row == -1:
            continue

        block_pang(row, col, new_map)

        dfs(depth + 1, new_map)

T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(H)]
    # print(map_arr)
    min_v = W * H

    dfs(0, map_arr)

    print(f'#{t} {min_v}')