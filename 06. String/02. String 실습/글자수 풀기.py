import sys
sys.stdin = open('글자수.txt')

T = int(input())
for test_case in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    cnt = {}

    for i in range(len(str1)):
        if str1[i] not in cnt:
            cnt[str1[i]] = 0
    # print(cnt)

    for i in range(len(str2)):
        if str2[i] in cnt:
            cnt[str2[i]] += 1
    # print(cnt)
    max_cnt = 0
    for i in cnt.values():
        if i > max_cnt:
            max_cnt = i
    print('#{} {}'.format(test_case, max_cnt))