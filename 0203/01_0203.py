"""
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
"""

def isWall(x, y):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return True
    else:
        return False

def calAbs(a, b):
    if a > b:
        return a - b
    else:
        return b - a

arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for y in range(5):
    for x in range(5):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[y][x],arr[testY][testX])