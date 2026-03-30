import sys
# sys.stdin = open("3190.txt", "r")
# from collections import deque

def game(sr, sc):
    global d, time

    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited[sr][sc] = 1
    row = sr
    col = sc
    q = list()
    q.append((row, col))

    while True:
        time += 1

        nr, nc = row + D[d][0], col + D[d][1]

        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc] == 1:
            break

        if (nr, nc) in apple_arr:
            apple_arr.remove((nr, nc))

        else:
            pr, pc = q.pop(0)
            visited[pr][pc] = 0

        if time in C:
            if C[time] == "L":
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4

        visited[nr][nc] = 1
        q.append((nr, nc))
        row, col = nr, nc

# T = int(input())

# for t in range(1, T + 1):
N = int(input())
K = int(input())
apple_arr = list()

for _ in range(K):
    r, c = map(int, input().split())
    apple_arr.append((r - 1, c - 1))

    # print(apple_arr)
L = int(input())
C = dict()
d = 0
time = 0

for _ in range(L):
    x, c = map(str, input().split())

    C[int(x)] = c

visited = [[0] * N for _ in range(N)]
    # print(visited)

game(0, 0)

print(time)