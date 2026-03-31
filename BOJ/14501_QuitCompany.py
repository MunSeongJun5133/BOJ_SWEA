def dfs(depth, sum_v):
    global max_v

    if depth >= N + 1:
        max_v = max(sum_v, max_v)
        return

    if T[depth] == 1 or depth + T[depth] <= N + 1:
        dfs(depth + T[depth], sum_v + P[depth])
    dfs(depth + 1, sum_v)

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
max_v = 0

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

# print(T, P)
dfs(1, 0)

print(max_v)