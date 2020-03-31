import sys
sys.stdin = open('글자수.txt')

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = {}

    for i in str1:
        if i not in cnt:
            cnt[i] = 0

    for i in str2:
        if i in cnt:
            cnt[i] += 1

    max_cnt = 0
    for i in cnt.values():
        if i > max_cnt:
            max_cnt = i
    print('#{} {}'.format(test_case, max_cnt))