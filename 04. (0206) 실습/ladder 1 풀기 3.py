def isWall(data, x, y, visited):
    if x < 0 or x >= 100:
        return False
    if y < 0 or y >= 100:
        return False
    if data[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

import sys
sys.stdin = open('(1210)Ladder1_input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    # 시작점 찾기
    for k in range(len(data)):
        if data[0][k] == 1:
            x = 0
            y = k
        # 움직이기
        visited = [[0 for _ in range(100)] for _ in range(100)]
        while True:
            visited[x][y] = 1
            dx = [0, 0, 1]  # 좌, 우, 하
            dy = [-1, 1, 0]
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if isWall(data, nx, ny, visited) == True:
                    x = nx
                    y = ny
                    visited[x][y] = 1
                    break
            if x == len(data) - 1:
                break
        if data[x][y] == 2:
            print('#{} {}'.format(test_case, k))
            break