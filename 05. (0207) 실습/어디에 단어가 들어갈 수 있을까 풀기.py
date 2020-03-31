import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt')

T = int(input())
for test_case in range(1, 1+1):
    N, K = map(int, input().split())
    temp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    data = [list(map(int, input().split())) for _ in range(N)]


    garo = 0
    for x in range(len(data)):
        for y in range(len(data[x]) - K + 1):
            cnt = 0
            for i in range(y, y+K):
                if data[x][i] == 1:
                    cnt += 1
            print(cnt)
        print()
            if cnt == K:
                data[x][i+1] != 0
    #             garo += 1
    # print(garo)