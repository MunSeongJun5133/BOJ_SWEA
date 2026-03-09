import sys
sys.stdin = open("26407.txt", "r")
from collections import deque

def bfs():
    while q:
        current = q.popleft()

        for next in skill_arr[current]:
            required[next] -= 1
            if not visited[next] and required[next] == 0:
                visited[next] = visited[current] + 1
                q.append(next)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    skill_arr = [[] for _ in range(N + 1)]
    required = [0] * (N + 1)
    visited = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        skills = list(map(int, input().split()))
        required[i] = skills[0]

        for j in range(1, len(skills)):
            pre = skills[j]
            skill_arr[pre].append(i)
        # print(skill_arr)

    for i in range(1, len(required)):
        if required[i] == 0:
            q.append(i)
            visited[i] = 1

    # print(skill_arr)
    # print(required)
    bfs()

    if max(required) > 0:
        print(f'#{t} {-1}')
        continue

    print(f'#{t} {max(visited)}')