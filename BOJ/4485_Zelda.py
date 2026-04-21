from heapq import heappop, heappush

def dijkstra():
    pq = list()
    heappush(pq, (map_arr[0][0], 0, 0))
    weight = [[float('inf')] * N for _ in range(N)]
    # print(weight)
    weight[0][0] = map_arr[0][0]

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
                    heappush(pq, (cost, nr, nc))

    return weight

i = 1

while True:
    N = int(input())

    if N == 0:
        break

    map_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(map_arr)

    result = dijkstra()

    print(f"Problem {i}: {result[N - 1][N - 1]}")

    i += 1