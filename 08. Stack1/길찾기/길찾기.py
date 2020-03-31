import sys
sys.stdin = open('길찾기.txt')
def prin(x):
    for i in range(len(x)):
        print(*x[i])

def isRoad(x, y):
    if x < 0 or x > 99:
        return False
    if y < 0 or y > 99:
        return False
    if G[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    else:
        return True

def dfs(start, end):
    s = []
    while True:
        for j in range(99, -1, -1):
            if isRoad(start, j):
                s.append(j)
                if end in s:
                    return 1
        if len(s) != 0:
            y = s.pop()
            visited[start][y] = 1 # 방문체크
            start = y
        else:
            return 0

for test_case in range(1, 11):
    no = map(int, input().split())
    data = list(map(int, input().split()))
    G = [[0 for _ in range(100)] for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]
    start, end = 0, 99

    # 인접행렬 저장
    for i in range(0, len(data), 2):
        G[data[i]][data[i+1]] = 1
    print('#{} {}'.format(test_case, dfs(start, end)))