import sys
sys.stdin = open("4123.txt", "r")

def calculate(arr):
    if arr[1] == '+':
        return int(arr[0] + arr[2])
    elif arr[1] == '-':
        return int(arr[0] - arr[2])
    elif arr[1] == '*':
        return int(arr[0] * arr[2])
    elif arr[1] == '/':
        return int(arr[0] / arr[2])


def bt(depth):
    global max_v
    global min_v
    if depth == N - 1:
        last = 0
        result = list()

        while len(num_arr) > last:
            result.append(num_arr[last])
            if len(result) == 3:
                result = [calculate(result)]

            if len(sequnce) > last:
                result.append(sequnce[last])
            last += 1

        max_v = max(result[0], max_v)
        min_v = min(result[0], min_v)

        return

    pre = None

    for idx in range(len(STACK)):
        if STACK[idx] == pre:
            continue

        if not visited[idx]:
            pre = STACK[idx]
            visited[idx] = 1
            sequnce.append(STACK[idx])
            bt(depth + 1)
            visited[idx] = 0
            sequnce.pop()

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    num_arr = list(map(int, input().split()))
    operator = {0 : '+', 1 : '-', 2 : '*', 3 : '/'}
    STACK = list()
    sequnce = list()
    max_v = -100000000
    min_v = 100000000
    visited = [0] * (N - 1)
    memo = list()

    for op in range(len(op_cnt)):
        for i in range(op_cnt[op]):
            STACK.append(operator[op])

    STACK.sort()
    bt(0)

    print(f'#{t} {max_v - min_v}')