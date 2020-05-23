import sys
sys.stdin = open('단지번호붙이기.txt')

def prin(a):
    for i in range(len(a)):
        print(*a[i])

def check(x, y):
    global N
    if x < 0 or x > N:
        return False
    if y < 0 or y > N:
        return False
    if G[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

def dfs(x, y):
    stack = []
    cnt = 0
    while True:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) == True:
                stack.append([nx, ny])
                visited[nx][ny] = 1
        if stack:
            x, y = stack.pop()
            cnt += 1
        else:
            return cnt

def Solve():
    global N
    result = []
    for x in range(N):
        for y in range(N):
            if check(x, y) == True:
                cnt = dfs(x, y)
                result.append(cnt)
    return result

N = int(input())
G = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input()))
    G.append(temp)
print(G)
print(Solve())
