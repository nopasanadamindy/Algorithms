
#### - Ladder2
​
>Ladder1과 달리 여러 번 사다리를 타야하므로 visit를 탈 때마다 초기화 해주어야 한다.
​
```python
## x : 세로 / y : 가로
def check(x, y, visit):
    if x < 0 or x >= SIZE:  return False
    if y < 0 or y >= SIZE:  return False
    if data[x][y] == 0:     return False
    if visit[x][y] == 1:    return False
    return True
​
def getCnt(x, y):
    dx = [ 0, 0, 1]
    dy = [-1, 1, 0]  #왼쪽, 오른쪽, 아래쪽
    visit = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    cnt = 0
    # visit[x][y] = 1
​
    while (True):
        if x == SIZE - 1: break
        for j in range(3):
            nx = x + dx[j]
            ny = y + dy[j]
            if check(nx, ny, visit):
                x = nx
                y = ny
                visit[x][y] = 1
                cnt += 1
                break;
    return cnt
​
def solve(): # data[x][y]
    min = 0x7fffffff
    retu = 0
    cnt = 0
    for i in range(SIZE):
        if data[0][i]: ## 1을 찾으면
            cnt = getCnt(0, i) ## getCnt로 보낸다.
        if cnt < min : ## 여기의 cnt는 getCnt의 cnt와 다른 변수이다.
            min = cnt
            ret = i
    return ret
​
import sys
sys.stdin = open("(1211)Ladder2_input.txt")
T = 10
SIZE = 100
for tc in range(T):
    no = int(input())
    data=[list(map(int, input().split())) for _ in range(SIZE)]
    # visit = [[0 for _ in range(SIZE)]for _ in range(SIZE)]
    print("#{} {}".format(tc+1,solve()))
