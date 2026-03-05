import sys
sys.stdin = open("1240.txt", "r")

def get_end(arr):
    for row in range(N - 1, -1, -1):
        for col in range(M - 1, -1, -1):
            if arr[row][col] == 1:
                return row, col

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    bit_arr = [list(map(int, input().strip())) for _ in range(N)]
    num_bit = {"0001101" : 0,
               "0011001" : 1,
               "0010011" : 2,
               "0111101" : 3,
               "0100011" : 4,
               "0110001" : 5,
               "0101111" : 6,
               "0111011" : 7,
               "0110111" : 8,
               "0001011" : 9}

    er, ec = get_end(bit_arr)
    sc = ec - 55

    code_arr = bit_arr[er]
    code = ''
    even = 0
    odd = 0

    for i in range(sc, ec + 1):
        code += str(code_arr[i])

    for i in range(0, 8):
        start = i * 7
        end = start + 7
        if (i + 1 ) % 2 == 0:
            even += num_bit[code[start:end]]
        else:
            odd += num_bit[code[start:end]]
    
    
    if (odd * 3 + even) % 10 == 0:
        print(f'#{t} {even + odd}')
    else:
        print(f'#{t} {0}')
    