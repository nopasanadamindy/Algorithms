import sys
sys.stdin = open('부분집합의합_input.txt')

T = int(input())
for test_case in range(1, T+1):
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    N, K = map(int, input().split())

    for i in range(1 << len(A)):
        bubun = []
        for j in range(len(A)):
            if i & (1 << j):
                bubun.append(A[j])

        if len(bubun) == N:
            hap = 0
            for k in range(N):
                hap += bubun[k]
            print(hap)
            # print(hap)
            # if hap == K:
             #     print('#{} {}'.format(test_case, 1))
            # else:
            #     print()