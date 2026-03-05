import sys
sys.stdin = open("5185.txt", "r")

def find_bin(num):
    bin_arr = [1, 2, 4, 8]

    for i in range(1 << len(bin_arr)):
        sum = 0
        result = ""

        for j in range(len(bin_arr)):
            if i & (1 << j):
                sum += bin_arr[j]
                result = '1' + result
            else:
                result = '0' + result


        if sum == num:
            # print(result)
            return result


T = int(input())

for t in range(1, T + 1):
    n, hexadecimal = map(str, input().split())
    N = int(n)
    hexadigits = "ABCDEF"
    hexa = {'A' : 10,
            'B' : 11,
            'C' : 12,
            'D' : 13,
            'E' : 14,
            'F' : 15}
    result = ""
    # print(n, hexadecimal)

    for i in range(N):
        if hexadecimal[i] not in hexadigits:
            result += find_bin(int(hexadecimal[i]))
        elif hexadecimal[i] in hexadigits:
            result += find_bin(hexa[hexadecimal[i]])

    print(f'#{t} {result}')

