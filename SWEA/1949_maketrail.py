import sys
sys.stdin = open("1949.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())