import sys
sys.stdin = open("2819.txt", "r")

def dfs(row, col, depth):
    global cnt, num_str

    if (row, col, tuple(num_str)) in subset:
        return
    subset.add((row, col, tuple(num_str)))

    if depth == 7:
        result.add(tuple(num_str))
        return

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 4 and 0 <= nc < 4:
            num_str.append(map_arr[nr][nc])
            dfs(nr, nc, depth + 1)
            num_str.pop()

T = int(input())

for t in range(1, T + 1):
    map_arr = [list(input().split()) for _ in range(4)]
    # print(map_arr)
    subset = set()
    result = set()
    num_str = list()
    cnt = 0

    for row in range(4):
        for col in range(4):
            num_str.append(map_arr[row][col])
            dfs(row, col, 1)
            num_str.pop()
    # print(*result)
    print(f'#{t} {len(result)}')