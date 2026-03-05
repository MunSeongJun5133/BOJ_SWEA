import sys
sys.stdin = open("5186.txt", "r")

def calculator(num):
    global result
    global cnt
    
    if num < 1e-12:
        return

    if cnt == 12:
        result = 'overflow'
        return

    if num * 2 >= 1:
        result += '1'
        num = (num * 2) - 1

    elif num * 2 < 1:
        result += '0'
        num *= 2

    cnt += 1
    calculator(num)


T = int(input())

for t in range(1, T + 1):
    N = float(input())
    result = ""
    cnt = 0

    if N == 0:
        print(f'#{t} 0')
        continue

    calculator(N)
    print(f'#{t} {result}')