
def isWall(x, y):
    if x < 0 or x >= SIZE:
        return True
    if y < 0 or y >= SIZE:
        return True
    return False

def abs(x, y):
    if x > y:
        return x - y
    else:
        return y - x


import sys
sys.stdin = open('dxdy.txt')

SIZE = 5
data = [list(map(int, input().split())) for _ in range(5)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sum = 0

for x in range(SIZE):
    for y in range(SIZE):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if isWall(nx, ny) == False:
                sum += abs(data[nx][ny], data[x][y])
print(sum)
