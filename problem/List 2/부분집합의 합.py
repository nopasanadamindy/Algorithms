import sys
sys.stdin = open('색칠하기.txt')


T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << n):
        #1. 부분집합 리스트로 만들기
        bubun = []
        for j in range(n + 1):
            if i & (1 << j):
                bubun.append(A[j])
        # print(bubun)
        #2. 부분집합 합 구하기
        sum_bubun = 0
        for k in range(len(bubun)):
            sum_bubun += bubun[k]
        # print(sum_bubun)
        #3. N,K조건에 맞는 것 cnt하기

        if len(bubun) == N and sum_bubun == K:
            cnt += 1
    print('#{} {}'.format(test_case, cnt))