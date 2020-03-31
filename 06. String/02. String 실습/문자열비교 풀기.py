def brute(str1, str2):
    for i in range(len(str2) - len(str1) + 1):
        cnt = 0
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                break
            else:
                cnt += 1
        if cnt == len(str1):
            return 1
    return 0

import sys
sys.stdin = open('문자열비교.txt')

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(test_case, brute(str1, str2)))




