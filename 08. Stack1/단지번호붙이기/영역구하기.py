import sys
sys.stdin = open('영역구하기.txt')
def prin(a):
    for i in range(len(a)):
        print(*a[i])

def paintColor(x1, x2, y1, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            G[x][y] = 1
    return G

def check(x, y):
    if x < 0 or x > N - 1:
        return False
    if y < 0 or y > M - 1:
        return False
    if G[x][y] == 1:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

def getCnt(x, y): #0을 카운팅해야한다.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    s = []
    cnt = 1
    while True:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) == True:
                s.append([nx, ny])
        if s:
            x, y = s.pop()
            if visited[x][y] == 0:
                cnt += 1
        else:
            return cnt

def Solve():
    ans = []
    for x in range(N):
        for y in range(M):
            if check(x, y) == True:
                cnt = getCnt(x, y)
                ans.append(cnt)
    return ans


N, M, K = map(int, input().split())
G = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    paintColor(x1, x2, y1, y2)
result = Solve()
ans = sorted(result)
print(len(ans))
print(*ans)