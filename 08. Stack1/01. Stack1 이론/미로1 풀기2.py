import sys
sys.stdin = open('미로1.txt')

def isWall(x, y, result):
    global visited
    if x < 0 and x > 15:
        return False
    if y < 0 and y > 15:
        return False
    if result[x][y] == 1:
        return False
    if visited[x][y] == 1:
        return False
    return True

# 스타트포인트 찾기
def findStart(result):
    for x in range(16):
        for y in range(16):
            if result[x][y] == 2:
                return x, y

# 옮겨다니기
def Solve(x, y, result):
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]
    s = []
    while True:
        visited[x][y] = 1 # 방문체크
        for i in range(4): # 방향체크
            nx = x + dx[i]
            ny = y + dy[i]
            if isWall(nx, ny, result) == True:
                s.append([nx, ny])
                if result[nx][ny] == 3:
                    return 1
        if len(s) != 0:
            x, y = s.pop()
        else:
            return 0

T = 10
for test_case in range(1, T+1):
    t_c = input()
    visited = [[0 for _ in range(16)] for _ in range(16)]
    result = []

    # data 저장
    for i in range(16):
        data = list(map(int, input()))
        result.append(data)

    x, y = findStart(result)
    ans = Solve(x, y, result)
    print('#{} {}'.format(test_case, ans))