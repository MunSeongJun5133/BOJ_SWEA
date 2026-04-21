import sys
sys.stdin = open("1251.txt", "r")
from heapq import heappush, heappop

# def prim(startnode):
#     visited = [False] * N
#     cnt = 0
#     total = 0
#
#     pq = list()
#     heappush(pq, (0, startnode))
#
#     while pq:
#         weight, current = heappop(pq)
#
#         if visited[current]:
#             continue
#
#         visited[current] = True
#         cnt += 1
#         total += weight
#
#         if cnt == N:
#             break
#
#         for nextnode in range(N):
#             if not visited[nextnode]:
#                 cost = ((X[current] - X[nextnode]) ** 2 + (Y[current] - Y[nextnode]) ** 2) * E
#                 heappush(pq, (cost, nextnode))
#     return total

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_x != ref_y:
        if ref_x < ref_y:
            parent[ref_x] = ref_y
        else:
            parent[ref_y] = ref_x
        return True
    return False

def kruskal():
    total = 0
    cnt = 0

    while edges:
        w, node1, node2 = heappop(edges)

        if union(node1, node2):
            total += w
            cnt += 1
            if cnt == N - 1:
                break
    return total

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    edges = list()

    for i in range(N - 1):
        for j in range(i + 1, N):
            cost = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) * E
            heappush(edges, (cost, i, j))

    parent = list(i for i in range(N))
    # print(parent)

    # result = prim(0)
    result = kruskal()

    print(f"#{t} {int(result + 0.5)}")