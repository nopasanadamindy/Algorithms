import sys
sys.stdin = open('단지번호.txt')

def check(x, y):
    global N
    if x < 0 or x > N-1: return False
    if y < 0 or y > N-1: return False
    if data[x][y] == 0: return False
    if visited[x][y] == 1: return False
    return True

def getCnt(x, y):
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    s = []
    cnt = 1
    while True:
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if check(nx, ny) == True:
                s.append([nx, ny])
        if len(s) != 0:
            x, y = s.pop()
            if visited[x][y] == 0:
                cnt += 1
        else:
            return cnt

def Solve():
    global N
    result = []
    for i in range(N):
        for j in range(N):
            if check(i, j) == True:
                cnt = getCnt(i, j)
                if cnt != 0:
                    result.append(cnt)
    return result

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
ret = Solve()
ans = sorted(ret)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
