import sys
sys.stdin = open("1767.txt", "r")

def dfs(depth, core_cnt, sum_v):
    global min_v, max_core

    if core_cnt + (cnt - depth) < max_core:
        return

    if depth == cnt:
        if core_cnt > max_core:
            max_core = core_cnt
            min_v = sum_v
        elif core_cnt == max_core:
            min_v = min(min_v, sum_v)
        return

    row, col = q[depth]

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = row + dr
        nc = col + dc
        count_v = 0
        path = []

        while 0 <= nr < N and 0 <= nc < N:
            if cell_arr[nr][nc] != 0:
                for r, c in path:
                    cell_arr[r][c] = 0
                break

            cell_arr[nr][nc] = 2
            path.append((nr, nc))
            count_v += 1

            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                dfs(depth + 1, core_cnt + 1, sum_v + count_v)
                for r, c in path:
                    cell_arr[r][c] = 0
                break

            nr = nr + dr
            nc = nc + dc


    dfs(depth + 1, core_cnt, sum_v)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cell_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(cell_arr)
    min_v = N * N
    q = list()
    cnt = 0
    max_core = 0

    for row in range(N):
        for col in range(N):
            if cell_arr[row][col] == 1:
                if row == 0 or row == N - 1 or col == 0 or col == N - 1:
                    continue
                q.append((row, col))
                cnt += 1

    dfs(0, 0, 0)

    print(f'#{t} {min_v}')