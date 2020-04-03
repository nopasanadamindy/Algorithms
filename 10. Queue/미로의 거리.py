import sys
sys.stdin = open('미로.txt')
from _collections import deque

def check(x, y):
    if x < 0 or x > N-1:
        return False
    if y < 0 or y > N-1:
        return False
    if data[x][y] == 1:
        return False
    if visited[x][y] != 0:
        return False
    else:
        return True

def prin(a):
    for i in range(len(a)):
        print(*a[i])

def startPoint():
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                return x, y

def bfs(x, y):
    que = deque() #1. queue 생성,  #2. visited 생성
    visited[x][y] = 1  # 4. 첫번째 인자 visited 체크
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    while True:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) == True:
                que.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if data[nx][ny] == 3:
                    return visited[x][y] + 1 -2
        if que:
            x, y = que.popleft() # append에 넣자마자 visited를 체크해주니까 가능

        else:
            return 0

    # que = deque() #1. queue 생성,  #2. visited 생성
    # que.append([x, y])  #3. 첫번째 인자 queue넣기(enque)
    # visited[x][y] = 1 #4. 첫번째 인자 visited 체크
    #
    # dx = [-1, 1, 0, 0] # 상하좌우
    # dy = [0, 0, -1, 1]
    # while que:   #5. while문
    #     x, y = que.popleft() # 6. deque
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #         if check(nx, ny) == True:
    #             que.append([nx, ny])
    #             print(que)
    #             visited[nx][ny] = (visited[x][y] + 1)
    #             prin(visited)
    #             if data[nx][ny] == 3:
    #                 return visited[nx][ny]
    #     else:
    #         return 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    x, y = startPoint()
    result = bfs(x, y)
    print('#{} {}'.format(test_case, result))
