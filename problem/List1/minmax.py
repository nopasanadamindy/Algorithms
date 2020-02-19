import sys
sys.stdin = open("minmax.txt")

T = int(input())
for tc in range(1, T + 1):
    length = int(input())
    num = list(map(int, input().split()))
    max_num = num[0]
    min_num = num[0]
    # max, min 구하기
    for i in range(len(num)):
        if num[i] >= max_num:
            max_num = num[i]
        if num[i] <= min_num:
            min_num = num[i]
    # 빼기
    result = max_num - min_num
    print('#{} {}'.format(tc, result))