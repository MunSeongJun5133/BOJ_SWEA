import sys
sys.stdin = open("17472.txt", "r")
from collections import deque

def check(r, c, start):
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = r + dr
        nc = c + dc
        length = 0

        while 0 <= nr < N and 0 <= nc < M:
            if island_arr[nr][nc] == 0:
                length += 1
            else:
                break
            
            nr = nr + dr
            nc = nc + dc
        

def bfs(r, c, n):
    q = deque()
    q.append((r, c))
    island_arr[r][c] = n

    while q:
        row, col = q.popleft()

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and island_arr[nr][nc] == 1:
                    visited[nr][nc] = n
                    island_arr[nr][nc] = n
                    q.append((nr, nc))

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    island_arr = [list(map(int, input().split())) for _ in range(N)]
    num = 1
    visited = [[0] * M for _ in range(N)]
    min_v = N * M
    # print(island_arr)

    for row in range(N):
        for col in range(M):
            if island_arr[row][col] == 1:
                visited[row][col] = num
                bfs(row, col, num)
                num += 1
    
    connected= []

    for row in range(N):
        for col in range(M):
            if island_arr[row][col] != 0:
                check(row, col, island_arr[row][col])