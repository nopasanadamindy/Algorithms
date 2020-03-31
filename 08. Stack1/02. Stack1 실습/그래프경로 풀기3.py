import sys
sys.stdin = open('그래프경로.txt')
def prin(a):
    for i in range(len(a)):
        print(*a[i])

def dfs(start, end):
    s = []
    visited[start] = 1 #방문체크
    while True:
        for w in range(V, 0 , -1): # 인접 탐색
            if G[start][w] == 1 and visited[w] == 0: # 조건 체크
                s.append(w) # 넣고
                if end in s:
                    return 1
        if len(s) != 0:
            start = s.pop()
        else:
            return 0

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        G[a][b] = 1
    start, end = map(int, input().split())
    print('#{} {}'.format(test_case, dfs(start, end)))