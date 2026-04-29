import sys
sys.stdin = open("1244.txt", "r")

def dfs(depth):
    global max_v

    state = (tuple(num_arr), depth)

    if state in result:
        return

    result.add((tuple(num_arr), depth))

    if depth == changes:
        middle = "".join(map(str, num_arr))
        max_v = max(max_v, int(middle))
        return

    for i in range(len(num_arr) - 1):
        for j in range(i + 1, len(num_arr)):
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
            dfs(depth + 1)
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]

T = int(input())

for t in range(1, T + 1):
    num, changes = map(int, input().split())
    num_arr = list(map(int, str(num).strip()))
    max_v = 0
    # print(num_arr)
    result = set()

    dfs(0)

    print(f"#{t} {max_v}")