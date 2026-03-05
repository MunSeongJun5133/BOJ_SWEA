import sys
sys.stdin = open("4366.txt", "r")

T = int(input())

for t in range(1, T + 1):
    bin = input()
    tri = input()
    # print(bin)
    # print(tri)
    B = set()
    result = 0

    for i in range(1, len(bin)):
        bnum = 0
        copy = list(bin)
        if copy[i] == '1':
            copy[i] = '0'
        else:
            copy[i] = '1'

        for j in range(len(copy)):
            bnum += (2 ** j) * int(copy[-1 - j])

        B.add(bnum)

    # print(B)

    for i in range(len(tri)):
        copy = list(tri)
        for j in ['0', '1', '2']:
            tnum = 0
            if tri[i] == j:
                continue

            copy[i] = j

            for k in range(len(copy)):
                tnum += (3 ** k) * int(copy[-1 - k])

            if tnum in B:
                result = tnum
                break
        if result != 0:
            break

    print(f'#{t} {result}')