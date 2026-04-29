import sys
sys.stdin = open("2819.txt", "r")

def dfs(row, col, result):
    if len(result) == 7:
        DP.add(result)
        return

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, result + map_arr[nr][nc])


T = int(input())

for t in range(1, T + 1):
    map_arr = [list(map(str, input().split())) for _ in range(4)]
    # print(map_arr)
    DP = set()

    for row in range(4):
        for col in range(4):
            dfs(row, col, map_arr[row][col])

    print(f"#{t} {len(DP)}")