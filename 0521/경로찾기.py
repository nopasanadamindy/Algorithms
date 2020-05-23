import sys
sys.stdin = open('경로찾기.txt')


def dfs(v):
    stack = []
    visited = [0 for _ in range(N)]
    while 1 :
        for w in range(len(G)):
            if G[v][w] == 1 and visited[w] == 0:
                stack.append(w)
                visited[w] = 1
        if len(stack) == 0:
            return visited
        else:
            v = stack.pop()

def prin(a):
    for i in range(len(a)):
        print(*a[i])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    G = []
    result = []

    for i in range(N):
        temp = list(map(int, input().split()))
        G.append(temp)

    for i in range(N):
        result.append(dfs(i))
    prin(result)