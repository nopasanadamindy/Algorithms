import sys
sys.stdin = open('(1221)GNS_input.txt')
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for test_case in range(1, T+1):
    N = input()
    data = list(map(str, input().split()))
    result = []
    for i in range(len(num)):
        for j in range(len(data)):
            if num[i] == data[j]:
                result.append(data[j])

# PrintSet
    # 1. join method
    # print('#{}'.format(test_case))
    # print(' '.join(result))

    # 2. for문 사용
    # print('#{}'.format(test_case))
    # for i in range(len(result)):
    #     print(result[i], end = ' ')
    # print()

    # 3. unpacking
    print('#{}'.format(test_case))
    print(*result)