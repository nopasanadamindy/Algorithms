import sys
sys.stdin = open('특별한 정렬.txt')

T = int(input())
for test_case in range(1, T+1):
    length = int(input())
    data = list(map(int, input().split()))
    result = []
    # 1. max값 min값 찾아내기
    for j in range(len(data)//2):
        maxi = data[0]
        mini = data[0]
        max_idx = 0
        min_idx = 0
        for i in range(len(data)):
            if data[i] >= maxi:
                maxi = data[i]
                max_idx = i
            if data[i] <= mini:
                mini = data[i]
                min_idx = i
    # 2. pop해서 result에 추가하기
        if max_idx > min_idx:
            max_pop = data.pop(max_idx)
            result.append(max_pop)
            min_pop = data.pop(min_idx)
            result.append(min_pop)
        else:
            min_pop = data.pop(min_idx)
            result.append(min_pop)
            max_pop = data.pop(max_idx)
            result.append(max_pop)
    print(result)
    # for i in range(len(result)):
    #         print(result[i], end = ' ')
    # print()
    # # print('{} {}'.format(test_case, result)