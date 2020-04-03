from _collections import deque
import sys
sys.stdin = open('노드.txt')

def BFS(start_node):
    global result
    Q.append(start_node)
    visited[start_node] = 1

    while Q:
        start_node = Q.pop(0)
        for next_node in range(1, v+1):
            if MyMap[start_node][next_node] and not visited[next_node]:
                Q.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start_node] +1
                if next_node == end_node:
                    result = distance[next_node]
                    return
    return

TC = int(input())
for tc in range(1, TC+1):
    v,e = map(int, input().split())
    MyMap = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    distance = [0] * (v+1)

    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1
        MyMap[end][start] = 1

    start_node, end_node = map(int, input().split())

    Q = []
    result = 0
    BFS(start_node)
    print(f'#{tc} {result}')

# def prin(a):
#     for i in range(len(a)):
#         print(*a[i])

# def bfs(x, end):
#     que = deque()
#     que.append(x)
#     visited[x] = 1
#     while que:
#         x = que.popleft()
#         for y in range(1, V+1):
#             if G[x][y] == 1 and visited[y] == 0:
#                 que.append(y)
#                 visited[x] = 1 ##
#                 far[y] = far[x] + 1
#                 if y == end:
#                     return
#     return
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     V, E = map(int, input().split())
#     data = []
#     G = [[0 for _ in range(V+1)] for _ in range(V+1)]
#     visited = [0 for _ in range(V+1)]
#     far = [0 for _ in range(V+1)]
#
#     for i in range(E):
#         a, b = map(int, input().split())
#         data.append(a)
#         data.append(b)
#     start, end = map(int, input().split())
#
#     # 인접행렬에 저장
#     for i in range(0, len(data), 2):
#         G[data[i]][data[i+1]] = 1
#         G[data[i+1]][data[i]] = 1
#     result = bfs(start, end)
#     print('#{} {}'.format(test_case, result))