def check(row, col):
    for r in range(row):
        if chessboard[r][col] == 1:
            return False

    for c in range(col):
        if chessboard[row][c] == 1:
            return False

    for i in range(1, row + 1):
        if 0 <= row - i < N and 0 <= col - i < N:
            if chessboard[row - i][col - i] == 1:
                return False

    for i in range(1, row + 1):
        if 0 <= row - i < N and 0 <= col + i < N:
            if chessboard[row - i][col + i] == 1:
                return False

    return True

def dfs(row, sum_v):
    global cnt_NQueen

    if row == N:
        if sum_v == N:
            cnt_NQueen += 1
        return

    for col in range(N):
        if check(row, col):
            chessboard[row][col] = 1
            dfs(row + 1, sum_v + 1)
            chessboard[row][col] = 0


N = int(input())
chessboard = [[0] * N for _ in range(N)]
# print(chessboard)
cnt_NQueen = 0

dfs(0, 0)

print(cnt_NQueen)