import sys
sys.stdin = open('색칠하기_input.txt')
def prin(a):
    for i in range(len(a)):
        print(*a[i])

T = int(input())
for test_case in range(1, T+1):
    area = int(input())
    G = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for i in range(area):
        x1, y1, x2, y2, color = map(int, input().split())
        # 색칠하기
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                G[i][j] += color
    # 카운팅
    for i in range(10):
        for j in range(10):
            if G[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(test_case, cnt))