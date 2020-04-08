import sys
sys.stdin = open('DFSBFS.txt')
from _collections import deque

def dfs(v):
    global N
    stack = []
    visited_d.append(v)
    while True:
        for w in range(N, 0, -1):
            if G[v][w] == 1 and w not in visited_d:
                stack.append(w)
        if stack:
            v = stack.pop()
            if v not in visited_d:
                visited_d.append(v)
        else:
            return visited_d

def bfs(v):
    que = deque()
    visited_b.append(v)
    que.append(v)
    while que:
        v = que.popleft()
        for w in range(N+1):
            if G[v][w] == 1 and w not in visited_b:
                que.append(w)
                visited_b.append(w)
    return visited_b

T = int(input())
for test_case in range(1, 1+1):
    N, M, V = map(int, input().split()) #   정점, 간선, 시작점
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited_d = []
    visited_b = []
    data = []
    for i in range(M):
        a, b = map(int, input().split())
        data.append(a)
        data.append(b)
    for i in range(0, len(data), 2):
        G[data[i]][data[i+1]] = 1
        G[data[i+1]][data[i]] = 1

    r_d = dfs(V)
    r_b = bfs(V)
    print(*r_d)
    print(*r_b)