import sys
sys.stdin = open("1242.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    code_arr = [list(input().strip()) for _ in range(N)]
    # print(code_arr)

    subset = set()

    for row in range(N):
        STACK = ""
        for col in range(M):
            if code_arr[row][col] != '0':
                STACK += code_arr[row][col]

        if STACK:
            subset.add(STACK)

    # print(subset)

    while subset:
        code = subset.pop()

        hex_code = int(code, 16)
        bin_code = bin(hex_code)
        print(bin_code)

        print(len(bin_code))