'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def DFS(v):
    # 방문체크
    visited[v] = 1

    # 인접 체크
    for w in range(V+1):
        if G[i][v] == 1 and visited[w] == 0:
            DFS(w)

V, E = map(int, input().split())
data = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
# print(data)

# 인접행렬 입력
for i in range(0, len(data), 2):
    G[data[i]][data[i+1]] = 1
    G[data[i+1]][data[i]] = 1

for i in range(V+1):
    print('{} {}'.format(i, G[i]))

# V, E = map(int, input().split())
# data = list(map(int, input().split()))
# G = [[0 for _ in range(V+1)] for _ in range(V+1)]
# visited = [0 for _ in range(V+1)]
# # 인접행렬 값 추가
# for i in range(0, len(data), 2):
#     G[data[i]][data[i+1]] = 1
#     G[data[i+1]][data[i]] = 1
#
#
# # 입력확인i, G[i]))
# for i in range(V+1):
#     print('{} {}'.format(i, G[i]))