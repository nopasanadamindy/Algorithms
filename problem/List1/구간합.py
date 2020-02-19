import sys
sys.stdin = open("구간합.txt")
T = int(input())
for test_case in range(1, T + 1):
    max_sum = 0
    min_sum = 9999999999 #max_sum
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    for i in range(N - M + 1):
        s = 0
        k = i
        x = 0
        while x < M:
            s += num[k]
            k += 1
            x += 1
        if s >= max_sum:
            max_sum = s
        if s <= min_sum:
            min_sum = s
    # print(max_sum)
    # print(min_sum)

    result = max_sum - min_sum
    print('#{} {}'.format(test_case, result))