import sys
sys.stdin = open('스도쿠.txt')

T = int(input())
for test_case in range(1, 1+1):

    for _ in range(10):
        # data = list(map(int, input().split()))
        data = input().split()
        # print(data)

        # 가로 줄 검증
        # cnt_garo = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        # for x in range(len(data)):
        #     for y in range(len(data[0])):
        #         cnt_garo[data[x][y]] += 1
        # for i in cnt_garo.values():
        #     if i != 1:
        #         print('0')
        #         break
        #     else:
        #         continue

        # 세로 줄 검증
        # cnt_sero = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        # for y in range(len(data[0])):
        #     for x in range(len(data)):
        #         cnt_sero[data[x][y]] += 1
        # for i in cnt_sero.values():
        #     if i != 1:
        #         print('0')
        #         break
        #     else:
        #         continue
        # print(cnt_sero)

        # 네모칸 검증
        cnt_square = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for x in range(0, len(data), 3):
            x_i = int(x)
            for y in range(0, len(data), 3):
                y_i = int(y)
                for k in range(2):
                    cnt_square[str(data[x_i+k][y_i+k])] += 1
        print(cnt_square)

                # cnt = 0
                # while cnt < 2:
                #     cnt_square[data[x_i+cnt][y_i+cnt]] += 1
                #     print(data[x_i+cnt][y_i+cnt])
                #     cnt += 1
                # print(data[x_i+cnt][y_i+cnt])
        # print(cnt_square)
