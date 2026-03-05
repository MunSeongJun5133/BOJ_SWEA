import sys
sys.stdin = open("1953.txt", "r")
from collections import deque

def bfs(r, c):
    global time

    q = deque()
    q.append((r, c))
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    time += 1

    while q:
        if time > L:
            break
        row, col = q.popleft()

        D = delta[map_arr[row][col]]

        for dr, dc in D:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and map_arr[nr][nc] != 0:
                nD = delta[map_arr[nr][nc]]

                for dr, dc in nD:
                    nnr = nr + dr
                    nnc = nc + dc

                    if 0 <= nnr < N and 0 <= nnc < M and map_arr[nnr][nnc] != 0:
                        if nnr == row and nnc == col:
                            visited[nr][nc] = visited[row][col] + 1
                            time = visited[nr][nc]
                            q.append((nr, nc))
                            break
    
    cnt = 0

    for row in range(N):
        for col in range(M):
            if visited[row][col] <= L and visited[row][col] != 0:
                cnt += 1
    
    # print(visited)
    return cnt


T = int(input())

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(map_arr)
    time = 0

    delta = {1 : [(0, 1), (1, 0), (0, -1), (-1, 0)],
             2 : [(1, 0), (-1, 0)],
             3 : [(0, 1), (0, -1)],
             4 : [(0, 1), (-1, 0)],
             5 : [(0, 1), (1, 0)],
             6 : [(1, 0), (0, -1)],
             7 : [(0, -1), (-1, 0)]}

    print(f'#{t} {bfs(R, C)}')