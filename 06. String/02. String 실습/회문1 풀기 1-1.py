import sys
sys.stdin = open('회문1.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    # data = [list(input()) for _ in range(8)]
    data = [input() for _ in range(8)]
    # print(data)
    cnt = 0

    # 가로 회문 찾기
    for x in range(8):
        for y in range(8 - N + 1):
            temp = []
            for i in range(y, y+N):
                temp.append(data[x][i])
            # print(temp)
            if temp == temp[::-1]:
                cnt += 1
    for y in range(8):#len(data[0])
        for x in range(8-N+1): #len(data) - N + 1
            temp = []
            for k in range(x, x+N):
                temp.append(data[k][y])
            if temp == temp[::-1]:
                cnt += 1

    print(cnt)




    # 세로 회문 찾기
    # for j in range(len(data[0])):
    #     for i in range(len(data) - N + 1):
    #         result = []
    #         for k in range(i, i + N):
    #             result.append(data[k][j])
    #         if isPalindrome(result) == True:
    #             cnt+= 1
    # print('#{} {}'.format(test_case, cnt))