import sys
sys.stdin = open('회문1.txt')
# 수정
T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(8)]
    h_len = N // 2
    cnt = 0
    for y in range(8):
        for x in range(8 - N + 1):
            x_cnt = y_cnt = 0
            # 가로확인
            for i in range(h_len):
                if data[y][x + i] != data[y][x + N-1 -i]:
                    break
                x_cnt += 1
            # 세로확인
            for j in range(h_len):
                if data[x + j][y] != data[x + N-1 - j][y]:
                    break
                y_cnt += 1

            if x_cnt == h_len:
                cnt += 1
            if y_cnt == h_len:
                cnt += 1
    print('#{} {}'.format(test_case, cnt))
