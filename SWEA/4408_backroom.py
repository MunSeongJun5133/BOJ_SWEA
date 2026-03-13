import sys
sys.stdin = open("4408.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    corridor = [0] * 200

    for i in range(N):
        s, e = map(int, input().split())
        start = min((s - 1) // 2, (e - 1) // 2)
        end = max((s - 1) // 2, (e - 1) // 2)

        for i in range(start, end + 1):
            corridor[i] += 1

    min_v = max(corridor)

    print(f'#{t} {min_v}')