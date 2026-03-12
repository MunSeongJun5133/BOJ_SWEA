import sys
sys.stdin = open("1767.txt", "r")

def check(ro, co, dr, dc):
    nr = ro + dr
    nc = co + dc
    while 0 <= nr < N and 0 <= nc < N:
        if cell_arr[nr][nc] != 0:
            return False
        nr += dr
        nc += dc
    return True

def dfs(depth, c_count, w_length):
    global max_core, min_wire

    if c_count + (len(STACK) - depth) < max_core:
        return

    if depth == len(STACK):
        if max_core < c_count:
            max_core = c_count
            # print(max_core)
            min_wire = w_length
        elif max_core == c_count:
            min_wire = min(min_wire, w_length)
            # print(max_core)
        return
    
    row , col = STACK[depth]

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = row + dr
        nc = col + dc
        path = list()
        c = 0
        if not check(row, col, dr, dc):
            continue

        while 0 <= nr < N and 0 <= nc < N:
            # if cell_arr[nr][nc] != 0:
            #     for r, c in path:
            #         cell_arr[r][c] = 0
            #     break

            cell_arr[nr][nc] = 2
            c += 1
            path.append((nr, nc))

            # if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
            #     dfs(depth + 1, c_count + 1, w_length + c)
            #     for r, c in path:
            #         cell_arr[r][c] = 0

            nr += dr
            nc += dc

        dfs(depth + 1, c_count + 1, w_length + c)

        for r, c in path:
            cell_arr[r][c] = 0

    dfs(depth + 1, c_count, w_length)

        


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cell_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(cell_arr)
    max_core = 0
    min_wire = N * N
    STACK = list()

    for row in range(N):
        for col in range(N):
            if cell_arr[row][col] == 1:
                if (row == 0 or row == N - 1 or col == 0 or col == N - 1):
                    continue
                
                STACK.append((row, col))
                

    # print(core_cnt)
    # print(STACK)

    dfs(0, 0, 0)

    print(f'#{t} {min_wire}')