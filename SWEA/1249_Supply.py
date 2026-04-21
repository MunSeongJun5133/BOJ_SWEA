import sys
sys.stdin = open("1249.txt", "r")
from heapq import heappop, heappush

def dijkstra(sr, sc):
    weight = [[float('inf')] * N for _ in range(N)]
    # print(weight)
    weight[sr][sc] = 0
    pq = list()
    pq.append((weight[sr][sc], sr, sc))

    while pq:
        w, row, col = heappop(pq)

        if weight[row][col] < w:
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < N and 0 <= nc < N:
                cost = map_arr[nr][nc] + w

                if cost < weight[nr][nc]:
                    weight[nr][nc] = cost
                    heappush(pq,(cost, nr, nc))

    return weight

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    map_arr = [list(map(int, input().strip())) for _ in range(N)]
    # print(map_arr)

    weight = dijkstra(0, 0)

    print(f"#{t} {weight[N - 1][N - 1]}")
