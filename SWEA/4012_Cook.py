import sys
sys.stdin = open("4012.txt", "r")

def btr(bit, depth, idx):
    global  min_v

    if depth == N // 2:
        food_a = list()
        food_b = list()
        score_a = 0
        score_b = 0

        for j in range(N):
            if bit & (1 << j):
                food_a.append(j)
            else:
                food_b.append(j)

        for i in range(depth):
            for j in range(depth):
                score_a += point_arr[food_a[i]][food_a[j]]
                score_b += point_arr[food_b[i]][food_b[j]]

        min_v = min(abs(score_a - score_b), min_v)
        return

    for i in range(idx, N):
        btr(bit | (1 << i), depth + 1, i + 1)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    point_arr = [list(map(int, input().split())) for _ in range(N)]
    team = [0] * N
    min_v = 20000
    # print(point_arr)

    btr(0, 0, 0)

    print(f'#{t} {min_v}')