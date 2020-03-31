import sys
sys.stdin = open('그래프경로.txt')
def prin(a):
    for i in range(len(a)):
        print(*a[i])

def dfs(start):
    s = []
    result = []
    visited[start] = 1
    result.append(start)
    while True:
        for next in range(V, 0, -1):
            if G[start][next] == 1 and visited[next] == 0:
                s.append(next)
        if len(s) != 0:
            start = s.pop()
            visited[start] = 1
            result.append(start)
        else:
            return result

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        G[a][b] = 1
    start, end = map(int, input().split())
    # print('#{} {}'.format(test_case, dfs(start, end)))
    print(dfs(start))