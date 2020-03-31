import sys
sys.stdin = open('ladder2.txt')
def prin(x):
    for i in range(len(x)):
        print(*x[i])

def isRoad(x, y, data):
    if x < 0 and x > 99:
        return False
    if y < 0 and x > 99:
        return False
    if data[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

def Solve(x, y, data):
    dx = [0, 0, 1] # 좌, 우, 하
    dy = [-1, 1, 0]
    if data[0][y] == 1: # 시작점에서 시작
         while True:
            visited[x][y] = 1 # 방문체크
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if isRoad(nx, ny, data) == True:
                    if data[nx][ny] == 2:
                        return 1
                    x = nx
                    y = ny


T = 10
for test_case in range(1, 1+1):
    tc = int(input())
    data = []
    visited = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        temp = list(map(int, input().split()))
        data.append(temp)
    # prin(data)
