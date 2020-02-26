'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
# 정답 : 24

def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    else:
        False
def abs(a, b):
    if a > b:
        return a - b
    else:
        return b - a

data = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    data[i] = list(map(int, input().split()))

sum = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isWall(nx, ny) == True:
                continue
            else:
                sum += abs(data[x][y], data[nx][ny])
print(sum)



