import sys
sys.stdin = open('DFS.txt')

def prin(a):
   for i in range(len(a)):
       print(*a[i])

def dfs(v):
    global N
    s = []
    visited.append(v)
    while True:
        for w in range(N, 0, -1):
            if G[v][w] == 1 and w not in visited:
                s.append(w)
                # print(s)
        if s:
            v = s.pop()
            if v not in visited:
                visited.append(v)
        else:
            return


for test_case in range(1, 4):
    N, M, V = map(int, input().split())
    data = []
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = []

    # 데이터 저장
    for _ in range(M):
        a, b = map(int, input().split())
        data.append(a)
        data.append(b)

    # 인접행렬 저장
    for i in range(0, len(data), 2):
        G[data[i]][data[i+1]] = 1
        G[data[i+1]][data[i]] = 1
    # prin(G)
    dfs(V)
    print(*visited)

