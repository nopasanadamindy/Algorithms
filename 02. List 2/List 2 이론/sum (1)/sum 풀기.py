import sys
sys.stdin = open('(1209)Sum_input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    # print(data)

    result = 0
    # 가로 합구하기
    max_garo = 0
    for x in range(100):
        garo = 0
        for y in range(100):
            garo += data[x][y]
        if garo > max_garo:
            max_garo = garo

    # 세로 합구하기
    max_sero = 0
    for y in range(100):
        sero = 0
        for x in range(100):
            sero += data[y][x]
        if sero > max_sero:
            max_sero = sero

    # 대각선 합구하기 /
    max_sum_1 = 0
    for y in range(100):
        sum_1 = 0
        for x in range(100):
            if x + y == 99:
                sum_1 += data[x][y]
        if sum_1 > max_sum_1:
            max_sum_1 = sum_1

    # 대각선 합구하기 \
    max_sum_2 = 0
    for y in range(100):
        sum_2 = 0
        for x in range(100):
            if x == y:
                sum_2 += data[x][y]
        if sum_2 > max_sum_2:
            max_sum_2 = sum_2

    # if result < max_garo:
    #     result = max_garo
    #     if  result < max_sero:
    #         result = max_sero
    #         if result < max_sum_1:
    #             result = max_sum_1
    #             if result < max_sum_2:
    #                 result = max_sum_2
    print('#{} {}'.format(test_case, result))