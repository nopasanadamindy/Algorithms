import sys
sys.stdin = open('두개의 숫자열.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_sum = 0
    if len(B) > len(A):
        for i in range(len(B) - len(A) + 1):
            temp = 0
            for j in range(len(A)):
                temp += B[i+j] * A[j]
            # print(temp)
            if temp > max_sum:
                max_sum = temp

    else:
        for i in range(len(A) - len(B) + 1):
            temp = 0
            for j in range(len(B)):
                temp += A[i+j] * B[j]
            # print(temp)
            if temp > max_sum:
                max_sum = temp
    print('#{} {}'.format(test_case, max_sum))
