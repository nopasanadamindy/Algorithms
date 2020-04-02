import sys
sys.stdin = open('미로2.txt')
def prin(a):
    for i in range(len(a)):
        print(*a[i])
def check(x, y):
    if x < 0 or x > N-1:
        return False
    if y < 0 or y > N-1:
        return False
    if data[x][y] == 1:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

def startPoint():
    global N
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                return x, y

def findRoad(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    s = []
    while True:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) == True:
                s.append([nx, ny])
                if data[nx][ny] == 3:
                    return 1
        if s:
            x, y = s.pop()
        else:
            return 0



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # print(data)
    x, y = startPoint()
    print('#{} {}'.format(test_case, findRoad(x, y)))
