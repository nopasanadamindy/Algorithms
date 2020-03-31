import sys
sys.stdin = open('ladder2.txt')

def isRoad(x, y, visited):
    if x < 0 or x > 99:
        return False
    if y < 0 or y > 99:
        return False
    if data[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

def Solve(x, y):
    global visited
    dx = [0, 0, 1] # 좌, 우, 하
    dy = [-1, 1, 0]
    visited = [[0 for _ in range(100)] for _ in range(100)]  # visited 초기화
    cnt = 0
    while True:
        if x == 99:
            break
        for j in range(3):
            nx = x + dx[j]
            ny = y + dy[j]
            if isRoad(nx, ny, visited) == True:
                x = nx
                y = ny
                visited[x][y] = 1
                cnt += 1
    return cnt

def min_cnt():
    mini = 9999999999999999999
    cnt = 0
    ans = 0
    for i in range(100):
        if data[0][i] == 1: # 출발
            cnt = Solve(0, i)
        if cnt < mini:
            mini = cnt
            ans = i
    return ans

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    # 결과
    print('#{} {}'.format(test_case, min_cnt()))