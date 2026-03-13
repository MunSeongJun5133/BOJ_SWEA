import sys
sys.stdin = open("1861.txt", "r")
from collections import deque

def bfs(r, c):
    global max_v

    q = deque()
    q.append((r, c))
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    cnt = 1

    while q:
        row, col = q.popleft()

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and (square_room[nr][nc] == square_room[row][col] + 1):
                    visited[nr][nc] = 1
                    cnt += 1
                    q.append((nr, nc))

    if max_v <= cnt:
        subset.add(tuple((r, c, cnt)))
        max_v = cnt

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    square_room = [list(map(int, input().split())) for _ in range(N)]
    subset = set()
    max_v = 0

    for row in range(N):
        for col in range(N):
            bfs(row, col)

    result = list()

    while subset:
        row, col, c = subset.pop()

        if c == max_v:
            result.append(square_room[row][col])

    print(f'#{t} {min(result)} {max_v}')