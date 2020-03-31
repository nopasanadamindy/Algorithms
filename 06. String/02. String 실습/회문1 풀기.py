def isPalindrome(data):
    if data == data[::-1]:
        return True
    else:
        return False
# def isPalindrome(data):
#     str = ''    # 원본 str에 copy하기
#     for i in data:
#         str += i
#     for i in range(len(data)//2):   # data 바꾸기
#         data[i], data[len(data)-1-i] = data[len(data)-1-i], data[i]
#     result = ''
#     for i in data:  # 바꾼것 result에 넣기
#         result += i
#     if str == result:   # 판별하기
#         return True
#     else:
#         return False

import sys
sys.stdin = open('회문1.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(8)]
    cnt = 0

    # 가로 회문 찾기
    for i in range(len(data)):
        for j in range(len(data[i]) - N + 1):
            result = []
            for k in range(j, j + N):
                result.append(data[i][k])
            if isPalindrome(result) == True:
                cnt += 1

    # 세로 회문 찾기
    for j in range(len(data[0])):
        for i in range(len(data) - N + 1):
            result = []
            for k in range(i, i + N):
                result.append(data[k][j])
            if isPalindrome(result) == True:
                cnt+= 1
    print('#{} {}'.format(test_case, cnt))