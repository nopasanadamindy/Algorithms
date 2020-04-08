from _collections import deque
import sys
sys.stdin = open('노드.txt')

def prin(a):
    for i in range(len(a)):
        print(*a[i])

def bfs(x, end):
    que = deque()
    que.append(x)
    visited[x] = 1
    while que:
        x = que.popleft()
        for y in range(1, V+1):
            if G[x][y] == 1 and visited[y] == 0:
                que.append(y)
                visited[x] = 1 ##
                far[y] = far[x] + 1
                if y == end:
                    return
    return


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    data = []
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    far = [0 for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        data.append(a)
        data.append(b)
    start, end = map(int, input().split())

    # 인접행렬에 저장
    for i in range(0, len(data), 2):
        G[data[i]][data[i+1]] = 1
        G[data[i+1]][data[i]] = 1
    result = bfs(start, end)
    print('#{} {}'.format(test_case, result))