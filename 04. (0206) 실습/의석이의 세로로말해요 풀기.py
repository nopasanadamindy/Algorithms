import sys
sys.stdin = open('(5356)의석이의세로로 말해요_input.txt')

T = int(input())
for test_case in range(1, T+1):
    result = ['' for _ in range(50)]
    for _ in range(5):
        data = list(input())
        for i in range(len(data)):
            result[i] += data[i]
    print(result)
    #     for i in range(len(data)):
    #         result[i] += data[i]
    # # print(*result)
    # print('#{}'.format(test_case), end = ' ')
    # print(*result, sep = '')