import sys
sys.stdin = open('gugan.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    gugan = list(map(int, input().split()))

    min_res = 999999
    max_res = 0
    for i in range(len(gugan)-M+1):
        hap = 0
        for j in range(i, i+M):
            hap += gugan[j]
        if hap > max_res:
            max_res = hap
        if hap < min_res:
            min_res = hap
    res = max_res - min_res
    print('#{} {}'.format(test_case, res))