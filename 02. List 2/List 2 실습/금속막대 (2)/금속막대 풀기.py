import sys
sys.stdin = open('(1259)금속막대_input.txt')
T = int(input())
for test_case in range(1, 1+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = []
    # for i in range(N):
        # data 짝수 idx에서 1개만 있는 숫자 찾기

    for x in range(len(data)):
        if x % 2 == 0:
            even = x
        else:
            odd = x
            # print(even, odd)
            if data[even] != data[odd]:
                result.append(data[even])
                result.append(data[even+1])
    print(result)