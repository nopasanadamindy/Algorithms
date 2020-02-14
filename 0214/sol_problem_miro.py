​
#### - 미로1
​
>일종의 그래프이므로 탐색을 위해  ***DFS 이용***. 0 or 1이므로 결정 문제
​
```python
'''
16 x 16
'''
def maze(y, x):
    global flag
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
​
    # data[y][x] = 9 #방문표시 ## 사실 한 번만 지나가면 되므로 data 자체에 표시해도 된다.
    visit[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
​
        if ny < 0 or ny == N: continue
        if nx < 0 or nx == N: continue
        # if data[ny][nx] == 9 : continue
        if visit[ny][nx] == 1: continue
        if data[ny][nx] == 1 : continue
        if data[ny][nx] == 3:
            flag = 1
            return
        ## return 하면 바로 이전 dfs(ny, nx)로 돌아간다. return 하지 않아도 사실 상관없음
        ## ★ 여기서 끝나는 게 아니라는 것★에 주의하자.
        ## 즉, 첫 시작까지 돌아가고 끝난다.
        maze(ny, nx)
​
​
def findStart(data):
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                return y, x
            ## return 값은 1개 뿐이므로 실제로는 튜플 형식으로 리턴 된다는 것을 기억하자.
​
import sys
sys.stdin = open("(1226)미로1_input.txt", 'r')
T = 10
N = 16
for tc in range(T):
    flag = 0
    no = int(input())
    data = [list(map(int, input())) for _ in range(N)]  # 미로를 중첩리스트로 저장
    # data = [0 for _ in range(N)]
    # for i in range(N):
    #     data[i] = list(map(int, input()))
    visit = [[0 for _ in range(N)]for _ in range(N)]
​
    sy, sx = findStart(data)
    maze(sy, sx)
    print("#{} {}".format(tc+1, flag))