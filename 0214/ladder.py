
def check(x, y, visit):
    if x < 0 or x >= 100:
        return False
    if y < 0 or y >= 100:
        return False
    if data[x][y] == 0:
        return False
    if visit[x][y] == 1:
        return False
    return True


def getCnt(x, y): #visit
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    cnt = 0
    visit = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    visit[x][y] = 1
    while True:
        if x == SIZE - 1:
            break
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if check(nx, ny, visit): #
                x = nx
                y = ny
                visit[nx][ny] = 1
                cnt += 1
                break
    return cnt


def solve():
    cnt = 0
    min = 99999
    idx = 0
    for i in range(SIZE):
        if data[0][i] == 1:
            cnt = getCnt(0, i)
        if cnt < min:
            min = cnt
            idx = i
    return idx


import sys

sys.stdin = open('ladder.txt')

T = 10
SIZE = 100

for test_case in range(1, T + 1):
    not_use = int(input())
    data = [list(map(int, input().split())) for _ in range(SIZE)]

    print(solve())