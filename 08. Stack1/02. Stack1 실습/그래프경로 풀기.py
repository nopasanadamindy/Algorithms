import sys
sys.stdin = open("그래프경로.txt")


def dfs(v):
    global G, visited, V, E
    stack = []
    stack.append(v)
    while len(stack) != 0:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(V, 0, -1):
                if G[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    # 인접행렬 저장
    for i in range(E):
        a, b = map(int, input().split())
        G[a][b] = 1

    # 시작/끝
    start, end = map(int, input().split())
    dfs(start)
    # print(visited)

    # 값 검증
    if visited[end] == 1:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))

    # if end in result:
    #     print('#{} {}'.format(test_case, 1))
    # else:
    #     print('#{} {}'.format(test_case, 0))


