import sys
sys.stdin = open('(1259)금속막대_input.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    even = []
    odd = []
    result = []
    # data 짝수 idx에서 1개만 있는 숫자 찾기
    for i in range(len(data)):
        if i % 2 ==0:
            even.append(data[i])
        else:
            odd.append(data[i])
    for i in range(len(even)):
        if even[i] not in odd:
            result.append(even[i])
            break#####
    # print(odd)
    # print(even)
    #
    # for _ in range(N):
    #     for i in range(len(data)-1):
    #         if result[-1] == data[i]:
    #             result.append(data[i])
    #             result.append(data[i + 1])
    # result.pop(0)
    for _ in range(N):
        for i in range(len(even)):
            if result[-1] == even[i]:
                result.append(even[i])
                result.append(odd[i])
    result.pop(0)

    # print('#{}'.format(test_case), end = ' ')
    # print(*result)

    print('#{}'.format(test_case), *result)

    # # 연쇄적으로 가져오기

