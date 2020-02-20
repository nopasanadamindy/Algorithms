import sys
sys.stdin = open('미로.txt')

# 인덱스 벗어나지 않게
def check(x, y):
    if x < 0 or x >= N:
        return 0
    if not (0 <= y < N):
        return 0
    if data[x][y] == 1:
        return 0
    else:
        return 1

def FindMiro(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] #상하좌우

    if data[x][y] == 2: # 시작
        while data[x][y] != 3: # 도착점에 도착할 때까지
            for i in range(4): # 이동할거야
                nx = x + dx[i]
                ny = y + dy[i]
                if check(nx, ny): # 움직일수있으면 움직일거야
                    x = nx
                    y = ny
        if data[x][y] == 3:
            return 1
        else:
            return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = [[0 for _ in range(N)] for _ in range(N)]
    data = [list(map(int, input())) for _ in range(N)]
    # print(data)

    print(FindMiro())

