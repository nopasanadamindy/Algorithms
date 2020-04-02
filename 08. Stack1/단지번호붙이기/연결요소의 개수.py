import sys
sys.stdin = open('연결요소.txt')
def prin(a):
    for i in range(len(a)):
        print(*a[i])

def dfs(v):
    s = []
    visited.append(v)
    while True:
        for w in range(N, 0, -1):
            if G[v][w] == 1 and w not in visited:
                s.append(w)
        if s:
            v = s.pop()
            if v not in visited:
                visited.append(v)
        else:
            return

def Solve():
    cnt = 0
    for x in range(1, N+1):
        if x not in visited:
            dfs(x)
            cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = []
    G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited = []
    for i in range(M):
        a, b = map(int, input().split())
        data.append(a)
        data.append(b)

    # 인접 행렬 저장
    for j in range(0, len(data), 2):
        G[data[j]][data[j+1]] = 1
        G[data[j+1]][data[j]] = 1
    result = Solve()
    print(result)