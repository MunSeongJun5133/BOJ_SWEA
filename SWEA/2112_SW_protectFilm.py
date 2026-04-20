import sys
sys.stdin = open("2112.txt", "r")

def check_protect(arr):
    if K == 1:
        return True

    for col in range(W):
        cnt = 1
        check = False
        for row in range(1, D):
            if arr[row][col] == arr[row-1][col]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                check = True
                break
        if not check:
            return False
    return True

def dfs(sum_v, start):
    global min_v

    if min_v <= sum_v:
        return

    if check_protect(copy_arr):
        min_v = min(min_v, sum_v)
        return

    for i in range(start, D):
        backup = copy_arr[i]
        copy_arr[i] = drug_a
        dfs(sum_v + 1, i + 1)
        copy_arr[i] = backup

        copy_arr[i] = drug_b
        dfs(sum_v + 1, i + 1)
        copy_arr[i] = backup

T = int(input())

for t in range(1, T + 1):
    D, W, K = map(int, input().split())
    film_arr = [list(map(int, input().split())) for _ in range(D)]
    # print(film_arr)
    min_v = float('inf')
    # print(copy_arr)
    copy_arr = [row[:] for row in film_arr]
    drug_a = [0 for _ in range(W)]
    drug_b = [1 for _ in range(W)]

    dfs(0, 0)

    print(f'#{t} {min_v}')