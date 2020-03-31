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

# 스타트 포인트에서 옮겨다니기
def Solve(x, y, result):
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]
    stack = []
    while True:
        visited[x][y] = 1
        # print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isWall(nx, ny, result) == True:
                stack.append([x, y])
                x = nx
                y = ny
                if result[x][y] == 3:
                    return 1
                break
        else:
            if len(stack) == 0:
                return 0
            else:
                x,y = stack.pop()

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
    print(ans)



