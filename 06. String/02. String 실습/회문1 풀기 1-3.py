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
            for i in range(N):
                data[x:]
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