import sys
sys.stdin = open('이진탐색_input.txt')

T = int(input())
for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

# A가 몇번만에 찾는지
    start = 1
    end = P
    cnt_A = 0
    while start <= end:
        cnt_A += 1
        middle = (start + end) // 2
        if Pa == middle:
            break
        elif Pa < middle:
            end = middle
        else:
            start = middle
    # print(cnt_A)

# B가 몇번 만에 찾는지
    start = 1
    end = P
    cnt_B = 0
    while start <= end:
        cnt_B += 1
        middle = (start + end) // 2
        if Pb == middle:
            break
        elif Pb < middle:
            end = middle
        else:
            start = middle
    # print(cnt_B)

# 승부
    result = 0
    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_A > cnt_B:
        result = 'B'
    else:
        result = 0
    print('#{} {}'.format(test_case, result))
