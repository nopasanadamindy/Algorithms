import sys
sys.stdin = open("그래프경로.txt")
def prin(a):
    for i in range(len(a)):
        print(*a[i])

# def dfs(start):
#     global G, visited, V, E, result
#     visited[start] = 1
#     result.append(start)
#
#     for w in range(V+1):
#         if G[start][w] == 1 and visited[w] == 0:
#             dfs(w)


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    result =[]

    for i in range(E):
        a, b = map(int, input().split())
        G[a][b] = 1
    # prin(G)
    start, end = map(int, input().split())
    dfs(start)
    # print(result)

    # 값 검증
    if end in result:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))
