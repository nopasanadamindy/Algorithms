import sys
sys.stdin = open('회문.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    # print(data)
    ans = []
    # 가로 회문검사
    for x in range(len(data)):
        for y in range(len(data[x])-M+1):
            result1 = []
            for i in range(M):
                result1.append(data[x][y+i])
            # print(result)
            if result1 == result1[::-1]:
                ans.append(result1)
    # 세로 회문검사
    for y in range(len(data)):
        for x in range(len(data[y])-M+1):
            result2 = []
            for i in range(M):
                result2.append(data[x+i][y])
            if result2 == result2[::-1]:
                ans.append(result2)
    print(ans)
    # print('#{}'.format(test_case), end = ' ')
    # for i in ans:
    #     for j in i:
    #         print(j, end = '')
    #     print()

    # 가로 회문 검사(슬라이싱)
    # for x in range(N):
    #     for y in range(N-M+1):
    #         result = data[y-x:N-M+y]
    #         print(result)
    #         # if result == result[::-1]:
    #         #     print(result)