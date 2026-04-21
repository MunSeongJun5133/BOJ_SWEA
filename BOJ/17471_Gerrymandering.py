from collections import deque

def is_connected(target_group_num, current_group_assignment):
    nodes = list()

    for i in range(N):
        if current_group_assignment[i] == target_group_num:
            nodes.append(i)

    if not nodes:
        return False

    visited = [False] * N
    queue = deque([nodes[0]])
    visited[nodes[0]] = True
    count = 1

    while queue:
        curr = queue.popleft()

        for neighbor in adj[curr]:
            if current_group_assignment[neighbor] == target_group_num and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count == len(nodes)

def dfs(depth):
    global min_v

    if depth == N:
        if is_connected(0, group) and is_connected(1, group):
            sum0 = sum(populations[i] for i in range(N) if group[i] == 0)
            sum1 = sum(populations[i] for i in range(N) if group[i] == 1)
            min_v = min(min_v, abs(sum0 - sum1))
        return

    group[depth] = 0
    dfs(depth + 1)

    group[depth] = 1
    dfs(depth + 1)

N = int(input())
populations = list(map(int, input().split()))
adj = [[] for _ in range(N)]

for i in range(N):
    node_data = list(map(int, input().split()))
    # print(node_data)
    for j in range(1, node_data[0] + 1):
        adj[i].append(node_data[j] - 1)

# print(adj)

min_v = float('inf')
group = [0] * N

dfs(0)

if min_v == float('inf'):
    print(-1)
else:
    print(min_v)