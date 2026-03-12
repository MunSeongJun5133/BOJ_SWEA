import sys
sys.stdin = open("10580.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    line_arr = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : x[0])
    # print(line_arr)
    cnt = 0

    for i in range(N - 1):
        A = line_arr[i][0]
        B = line_arr[i][1]

        for j in range(i + 1, N):
            if line_arr[j][0] > A and line_arr[j][1] < B:
                cnt += 1

    print(f'#{t} {cnt}')