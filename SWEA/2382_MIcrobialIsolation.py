import sys
sys.stdin = open("2382.txt", "r")
from collections import deque

def reverse(delta):
    if delta == 1:
        return 2
    elif delta == 2:
        return 1
    elif delta == 3:
        return 4
    elif delta == 4:
        return 3

def move(que):
    q = deque()

    while que:
        row, col, m_c, d = que.popleft()
        dr, dc = D[d]

        nr = row + dr
        nc = col + dc

        if 0 <= nr < N and 0 <= nc < N:
            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                d = reverse(d)
                dr, dc = D[d]
                nr = row + dr
                nc = col + nc
                m_c = int(m_c / 2)


T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    micro_map = [[0] * N for _ in range(N)]
    # print(micro_map)
    D = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}
    q = deque()

    for i in range(K):
        row, col, mic_cnt, d = map(int, input().split())
        q.append((row, col, mic_cnt, d))

    