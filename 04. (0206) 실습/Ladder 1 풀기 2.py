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

def Solve(data):
    x, y, nx, ny = 0, 0, 0, 0
    # 시작점 찾기
    for i in range(len(data[0])):
        if data[0][i] == 1:
            i = y

        # 움직이기
            visited = [[0 for _ in range(100)] for _ in range(100)]
            while True:
                dx = [0, 0, 1]
                dy = [-1, 1, 0]
                for k in range(3):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if isWall(data, nx, ny, visited) == True:
                        x = nx
                        y = ny
                        visited[x][y] = 1
                        break




import sys
sys.stdin = open('(1210)Ladder1_input.txt')

T = 10
for test_case in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(100)]
    print("#{} {}".format(test_case, Solve(data)))