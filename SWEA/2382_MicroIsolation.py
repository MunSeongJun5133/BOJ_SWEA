import sys
sys.stdin = open("2382.txt", "r")
from collections import deque

def reverse_d(delta):
    if delta == 1:
        return 2
    elif delta == 2:
        return 1
    elif delta == 3:
        return 4
    elif delta == 4:
        return 3

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    mic_move = dict()
    D = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}
    q = deque()

    for _ in range(K):
        row, col, mic_cnt, d = map(int, input().split())
        mic_move[(row, col)] = (mic_cnt, mic_cnt, d)

    for _ in range(M):
        new_mic = dict()

        for (r, c), (cc, mc, d) in mic_move.items():
            row, col = (r, c)
            cur_cnt, max_cnt, delta = (cc, mc, d)

            dr, dc = D[delta][0], D[delta][1]

            nr, nc = row + dr, col + dc

            if cur_cnt == 0:
                continue

            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                cur_cnt //= 2
                delta = reverse_d(delta)

            max_cnt = cur_cnt

            if (nr, nc) not in new_mic:
                new_mic[(nr, nc)] = [cur_cnt, max_cnt, delta]
            else:
                if new_mic[(nr, nc)][1] < max_cnt:
                    new_mic[(nr, nc)][0] += cur_cnt
                    new_mic[(nr, nc)][1] = max_cnt
                    new_mic[(nr, nc)][2] = delta

                elif new_mic[(nr, nc)][1] > max_cnt:
                    new_mic[(nr, nc)][0] += cur_cnt

        mic_move = new_mic

    result = 0

    for k in mic_move.keys():
        result += mic_move[k][0]

    print(f"#{t} {result}")