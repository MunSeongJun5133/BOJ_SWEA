import sys
sys.stdin = open("2817.txt", "r")

def dfs(depth, start, sum_v):
    global cnt

    if sum_v > K:
        return

    if sum_v == K:
        cnt += 1
        return
    
    for i in range(start + 1, N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i, sum_v + A[i])
            visited[i] = 0

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    visited = [0 for _ in range(N)]
    # print(N, K)
    # print(A)

    for i in range(N):
        visited[i] = 1
        dfs(i, i, A[i])
        visited[i] = 0

    print(f"#{t} {cnt}")