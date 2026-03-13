import sys
sys.stdin = open("1952.txt", "r")

def dfs(depth, current):
    global min_v

    if depth >= 12:
        s_v = 0
        i = 0
        while i < 12:
            if current[i] == 0:
                s_v += (schedule[i] * cost[0])
                i += 1
            elif current[i] == 1:
                s_v += cost[1]
                i += 1
            elif current[i] == 2:
                s_v += cost[2]
                i += 3
            else:
                i += 1

        if s_v < min_v:
            min_v = s_v

        return

    for i in range(3):
        new_arr = [row for row in current]
        if i == 2:
            for j in range(3):
                if depth + j < 12:
                    new_arr[depth + j] = i
            dfs(depth + 3, new_arr)

            for j in range(3):
                if depth + j < 12:
                    new_arr[depth + j] = -1
        else:
            new_arr[depth] = i
            dfs(depth + 1, new_arr)
            new_arr[depth] = -1

T = int(input())

for t in range(1, T + 1):
    cost = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    visited = [-1] * 12
    # print(cost)
    # print(schedule)
    min_v = 3000 * 30 * 12

    dfs(0, visited)

    min_v = min(min_v, cost[3])

    print(f'#{t} {min_v}')
