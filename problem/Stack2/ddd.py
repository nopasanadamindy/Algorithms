# import sys
# sys.stdin = open('special.txt')
T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    num = list(map(int, input().split()))
    for j in range(length//2):
        max_num = num[0]
        min_num = num[0]
        max_idx = 0
        min_idx = 0
        result = []

        # 1. max값 min값 찾아내기
        for i in range(len(num)):
            if num[i] >= max_num:
                max_num = num[i]
                max_idx = i
            if num[i] <= min_num:
                min_num = num[i]
                min_idx = i

        # 2. pop해서 result에 추가하기
        max_pop = num.pop(max_idx)
        result.append(max_pop)
        min_pop = num.pop(min_idx)
        result.append(min_pop)

    print(result)