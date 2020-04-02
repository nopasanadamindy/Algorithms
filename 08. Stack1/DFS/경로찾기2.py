import sys
sys.stdin = open('경로찾기.txt')

def prin(a):
    for i in range(len(a)):
        print(*a[i])

def check(x, y, visited):
    global N
    if x < 0 or x > N -1:
        return False
    if y < 0 or y > N -1:
        return False
    if data[x][y] == 0:
        return False
    if visited[y] == 1:
        return False
    else:
        return True

def move(start, end):
    s = []
    visited = [0 for _ in range(N)]
    x = start
    while True:
        for y in range(N):
            if check(x, y, visited) == True:
                s.append(y)
                visited[y] = 1
                if end in s:
                    G[start][end] = 1
                    return
        if len(s) !=0:
            x = s.pop()
        else:
            G[start][end] = 0
            return
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
G = [[0 for _ in range(N)] for _ in range(N)]
# prin(data)
for x in range(N):
    for y in range(N):
        start, end = x, y
        move(start, end)
prin(G)