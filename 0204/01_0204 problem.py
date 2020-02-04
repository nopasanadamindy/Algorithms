
import sys
sys.stdin = open('0203.txt')

T = 10

for test_case in range(1, T + 1):
    length = int(input())
    data = list(map(int, input().split()))


result = 0
# 1. 행의 합
    for y in range 100:
        sum = 0
        for x in range 100:
            sum += data[y][x]
        if result < sum:
            result = sum


# 2. 열의 합
    for y in range 100:
        sum = 0
        for x in range 100:
            sum += data[x][y]
        if result < sum:
            result = sum

# 3. 대각선의  합
    #1) /
    sum = 0
    for x in range 100:
        sum += data[x][x]
    if result < sum:
        result = sum


    #2) \
    sum = 0
    for x in range 100:
        sum += data[x][99-x]
    if result < sum:
        result = sum

    print('#{} {}'.format(length, result))