# [DFS 알고리즘] : stack을 만들어서

visited[], stack[] # 초기화

DFS(v)
v 방문;
visited[v] # <- true
do



# [DFS 알고리즘 - 재귀]
# - 훨씬 간단
# - 실행 시간이 훨씬 길긴 함
DFS_Recursive(G, v) #v = vertex : 시작 정점

    visited[ v ] #< TRUE// v 방문 설정

    For each all w in adjaency(G,v) # v에 인접한 모든 정점(w)에 대해서
        IF visited[w] != True # 방문을 안했다면
            DFS_Recursive(G, w) # Recursive로 돌려라