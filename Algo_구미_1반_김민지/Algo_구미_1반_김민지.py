import sys
sys.stdin = open('input.txt')

def check(x, y):
    if x < 0 or x > 9:
        return False
    if y < 0 or y > 9:
        return False
    if visited[x][y] == 1:
        return False
    if data[x][y] == 0:
        return False
    else:
        return True

def dfs(x, y):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 상하좌우
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    s = []
    visited[x][y] = 1
    while True:
        # print(x, y)
        # print(s)
        cnt = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) == True:
                s.append([nx, ny])
        if s:
            nx, ny = s.pop()
            if visited[nx][ny] == 0:
                x = nx
                y = ny
                visited[x][y] = 1
                cnt += 1
        else:
            return cnt

def getCnt():
    result = []
    for x in range(10):
        for y in range(10):
            if check(x, y) == True:
                cnt = dfs(x, y)
                result.append(cnt)
    return result

T = int(input())
for test_case in range(1, T+1):
    data = []
    visited = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        temp = list(map(int, input().split()))
        data.append(temp)
    ans = getCnt()
    ans2 = len(ans)
    print('#{} {}'.format(test_case, ans2))
