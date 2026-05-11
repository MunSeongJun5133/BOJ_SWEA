import sys
sys.stdin = open("2806.txt", "r")

def check_queen(row, col):
    for i in range(row):
        if (visited[i] == col) or (abs(row - i) == abs(visited[i] - col)):
            return False
    return True

def dfs(depth):
    global cnt

    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        if check_queen(depth, i):
            visited[depth] = i
            dfs(depth + 1)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    visited = [0 for _ in range(N)]
    cnt = 0
    # print(visited)

    dfs(0)

    print(f"#{t} {cnt}")