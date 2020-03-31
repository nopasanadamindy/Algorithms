import sys
sys.stdin = open('(2001)파리퇴치_input.txt')

T = int(input())
for test_case in range(1, 1+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for x in range(N):
        for y in range(N - M + 1):
            temp1 = []
            for i in range(M):
                temp1.append(data[x][y+i])
            # print(temp1)
            result.append(temp1)
    # print(result)

    max_ans = 0
    for x in range(len(result) - N):

        for y in range(len(result) - N):

            for k in range(M):


        print(i)
    #     ans = (sum(result[i]) + sum(result[i+(N-1)]))
    #     if ans > max_ans:
    #         max_ans = ans
    # print('#{} {}'.format(test_case, max_ans))
