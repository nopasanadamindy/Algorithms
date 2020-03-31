import sys
sys.stdin = open('희토류.txt')
def prin(a):
    for i in range(len(a)):
        print(*a[i])

def check(x, y):
    if x < 0 or x > N-1:
        return False
    if y < 0 or y > N-1:
        return False
    if data[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

def getCnt(x, y):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1] #상하좌우 #왼위왼아오위오아
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    stack = []
    amount = data[x][y]
    cnt = 1
    while True:
        visited[x][y] = 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) == True and data[x][y] == data[nx][ny]:
                stack.append([nx, ny])
        if len(stack) != 0:
            x, y = stack.pop()
            if visited[x][y] == 0:
                cnt += 1
                amount += data[x][y]
        else:
            return cnt, amount

def Solve():
    global N
    max_amount = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and data[i][j] != 0:
                cnt, amount = getCnt(i, j)
                if amount > max_amount:
                    max_amount = amount
                    x, y = i, j
    return max_amount, x, y

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # prin(data)
    amount, x, y = Solve()
    cnt = amount//data[x][y]
    print('#{} {} {}'.format(test_case, amount, cnt))
