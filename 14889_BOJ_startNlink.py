def dfs(depth, start):
    global min_v

    if depth == N / 2:
        start_point = 0
        link_point = 0
        for i in range(N):
            for j in range(N):
                if team[i] and team[j]:
                    start_point += balance[i][j]
                elif not team[i] and not team[j]:
                    link_point += balance[i][j]
        
        min_v = min(min_v, (abs(start_point - link_point)))

    else:
        for i in range(start, N):
            team[i] = True
            dfs(depth + 1, i + 1)
            team[i] = False


N = int(input())
balance = [list(map(int, input().split())) for _ in range(N)]
team = [False] * N
# print(team)
# print(balance)
depth, start = 0, 0
min_v = 1000
dfs(depth, start)
print(min_v)