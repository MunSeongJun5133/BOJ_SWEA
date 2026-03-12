import sys
sys.stdin = open("20551.txt", "r")

T = int(input())

for t in range(1, T + 1):
    A, B, C = map(int, input().split())
    cnt = 0

    if B < 2 or C < 3:
        print(f'#{t} {-1}')
        continue

    if B >= C:
        cnt += ((B - C) + 1)
        B = C - 1

    if A >= B:
        cnt += ((A - B) + 1)
        A = B - 1

    if A > 0:
        print(f'#{t} {cnt}')

    else:
        print(f'#{t} {-1}')
