import sys
sys.stdin = open('회문1.txt')
# 세진
for test_case in range(1, 11):
    N = int(input())
    my_map = [input() for _ in range(8)]
    cnt = 0
    # 가로회문조사
    for r in range(8):
        for c in range(8 - N + 1):
            temp_h = []
            for i in range(N):
                temp_h.append(my_map[r][c+i])
            if temp_h == temp_h[::-1]:
                cnt += 1

    # 세로회문조사
    for r in range(8 - N + 1):
        for c in range(8):
            temp_v = []
            for i in range(N):
                temp_v.append(my_map[r+i][c])
            if temp_v == temp_v[::-1]:
                cnt += 1
    print('#{} {}'.format(test_case, cnt))